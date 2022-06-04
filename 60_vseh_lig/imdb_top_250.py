from bs4 import BeautifulSoup
import requests
import random
from math import log

URL = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
HTML_DOC = requests.get(URL)
HTML_DOC.encoding = 'utf-8'
htmlString = HTML_DOC.text

soup = BeautifulSoup(htmlString, 'html.parser')
a = []
# print(htmlString)
for rows in soup.find_all("td", class_="titleColumn"):
    a.append(str(rows.a.string))


def pairs(a):
    b = []
    for i in range(0, len(a), 2):
        b.append(tuple(a[i:i+2]))
    return b


def ch(b):
    # print(f'{b =}')
    a0 = b[0]
    a1 = b[1] if len(b) == 2 else None
    if a1:
        print(f'1.{a0}\n2.{a1}')
        return b[int(input())-1]
    return a0


def gen(a):
    c = []
    for i in a:
        c.append(ch(i))
    # print(f'{c =}')
    return c


t = [a[:]]
while len(a) > 1:
    random.shuffle(a)
    print('Round of 1 /', int(log(len(a), 2)))
    a = gen(pairs(a))
    t.append(a)
print(t)
