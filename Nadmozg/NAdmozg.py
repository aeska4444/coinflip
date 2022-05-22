from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from googletrans import Translator
from random import choices, sample
from json import dump, load
from musixmatch import Musixmatch
from youtubepy import Video
import webbrowser

# config = {
#     '1. easy': {'answ_opt': 2, 'chunk_size': 8, 'trans_chain': 'ru'},
#     '2. normal': {'answ_opt': 4, 'chunk_size': 4, 'trans_chain': 'de-ru'},
#     '3. hard': {'answ_opt': 6, 'chunk_size': 2, 'trans_chain': 'uz-ja-uk'}}

with open("config.json", "r") as json_file:
    config = load(json_file)

difficulty = config['difficulty']
show_lyrics = config['show_lyrics']
open_youtube = config['open_youtube']
game_loop = config['game_loop']
# except:
#     with open("config.json", "w") as json_file:
#         dump(difficulty, json_file)
try:
    with open("lists.json", "r") as json_file:
        playlists = load(json_file)
except:
    playlists = {}
    playlists['4riovLwMCrY3q0Cd4e0Sqp'] = []
sp = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        client_id='102ed884cf594a63803ffd77274ef1da',
        client_secret='c9e18637af7242f38cb7318de9837dee'))
musixmatch = Musixmatch('2db20351f74ea0c92f75c6159e9f92a5')
translator = Translator()

pl_id = '4riovLwMCrY3q0Cd4e0Sqp'


def list_name(pl_id):
    return sp.playlist(pl_id)['description'].split('.')[0]


print(f'\nSpotify id_playlist or list number:')
if playlists:
    for i, j in enumerate(playlists.keys()):
        print(f'\t{i + 1}. {list_name(j)}')
else:
    print(f'\t1. {list_name(pl_id)}')
tmp = input('\t')
if tmp.isnumeric():
    pl_id = list(playlists.keys())[int(tmp) - 1]
else:
    pl_id = tmp

print('Difficulty:')
for i, j in enumerate(difficulty):
    print(f'\n{i+1}. {j}')
diff = difficulty[int(input('\t')) - 1]


id = f'spotify:playlist:{pl_id}'
ids = []
offset = 0
while True:
    response = sp.playlist_items(id, offset=offset,
                                 fields='items.track.id,total',
                                 additional_types=['track'])
    if len(response['items']) == 0:
        break
    offset = offset + len(response['items'])
    for i in response['items']:
        ids.append(i['track']['id'])
playlists[pl_id] = ids
with open("lists.json", "w") as json_file:
    dump(playlists, json_file)


def loop(ids, diff):
    answ_opt, chunk_size, trans_chain = diff['answ_opt'], diff['chunk_size'], diff['trans_chain']
    choice = choices(ids, k=answ_opt)
    dick = []
    for i in choice:
        track = sp.track(f'spotify:track:{i}')
        dick.append((track['artists'][0]['name'], str(track['name'])))
    author, song = dick[0]
    search = ' - '.join(dick[0])
    # print(f'{song=}, {author=}')
    # print(f"{musixmatch.matcher_lyrics_get(song, author)['message']['body']}")
    ly_text = musixmatch.matcher_lyrics_get(song, author)['message']['body']
    if not ly_text:
        loop(ids, diff)
    ly_text = ly_text['lyrics']['lyrics_body'].split('...\n\n')[0]
    ly_text = '\n'.join(el.strip() for el in ly_text.split('\n') if el.strip())
    # print(ly_text)
    text_ch1 = []
    num_str = ly_text.count('\n')
    text_ch = ly_text.split('\n')
    # ch = int(num_str * chunk_size)
    # print(f'{num_str=},{ch=}')
    for i in range(0, num_str, chunk_size):
        text_ch1.append(text_ch[i:i + chunk_size])
    text = '\n'.join(choices(text_ch1, k=1)[0])
    langs = trans_chain.split("-")
    while langs:
        text = translator.translate(text, dest=f'{langs[0]}').text
        langs.pop(0)
    print(f'\nTranslate:\n{text}\n\nVariants:')
    temp = enumerate(sample(dick, k=len(dick)))
    for i, j in temp:
        print(f'\t{i + 1}. {" - ".join(j)}')
        if j == dick[0]:
            temp1 = i + 1
    if input('\t') == str(temp1):
        print("\n\t\tYEP!\n\n")
    else:
        print(f'\n\t\tNOP,\t{search}\n')
    if open_youtube:
        webbrowser.open_new_tab(Video(search).search())
    if show_lyrics:
        print(ly_text)


loop(ids, diff)
if game_loop:
    loop(ids, diff)
