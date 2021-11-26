"""
Брутфорс на основе времени отклика на запрос
"""
import itertools
import random
import string
import timeit
import collections
import numpy as np

allowed_chars = string.ascii_letters + " " + string.digits
password_database = {"sach0k": "put y0ur finger in my ass"}


def check_password(user, guess):
    actual = password_database[user]
    if len(guess) != len(actual):
        return False

    for i in range(len(actual)):
        if guess[i] != actual[i]:
            return False
    return True


def random_str(size):
    return ''.join(random.choices(allowed_chars, k=size))


def crack_length(user, max_len=50, verbose=False) -> int:
    trials = 2000
    times = np.empty(max_len)
    for i in range(max_len):
        i_time = timeit.repeat(stmt='check_password(user, x)',
                               setup=f'user={user!r};x=random_str({i!r})',
                               globals=globals(),
                               number=trials,
                               repeat=10)
        times[i] = min(i_time)

    if verbose:
        most_likely_n = np.argsort(times)[::-1][:5]
        print(most_likely_n, times[most_likely_n] / times[most_likely_n[0]])

    most_likely = int(np.argmax(times))
    return most_likely


def crack_password(user, length, verbose=False):
    guess = random_str(length)
    counter = itertools.count()
    trials = 1000
    while True:
        i = next(counter) % length
        for c in allowed_chars:
            alt = guess[:i] + c + guess[i + 1:]

            alt_time = timeit.repeat(stmt='check_password(user, x)',
                                     setup=f'user={user!r};x={alt!r}',
                                     globals=globals(),
                                     number=trials,
                                     repeat=10)
            guess_time = timeit.repeat(stmt='check_password(user, x)',
                                       setup=f'user={user!r};x={guess!r}',
                                       globals=globals(),
                                       number=trials,
                                       repeat=10)

            if check_password(user, alt):
                return alt

            if min(alt_time) > min(guess_time):
                guess = alt
                if verbose:
                    print(guess)


def main():
    inp = [input('user_password (ascii_letters & digits & space): ').split('_')]
    if len(inp[0]) == 2 and all(i for i in inp[0]):
        password_database.update(inp)
        print(inp, file=open('log.ini', 'a'))
    user = collections.deque(password_database, maxlen=1)[0]
    print(f'username: {user}')
    length = crack_length(user, verbose=True)
    print(f"pass most likely length {length}")
    input("close extra programs and press enter to continue...")
    start = timeit.default_timer()
    password = crack_password(user, length, verbose=True)
    print(f"password cracked:'{password}'")
    stop = timeit.default_timer()
    print(f'spent time\t{stop - start} sec')


if __name__ == '__main__':
    main()
