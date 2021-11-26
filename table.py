"""
создание и заполнение таблицы с настраиваимымми параметрами
"""
from config import *


def table_draw(l, c, scale_l, scale_c, apart, fill, tab):
    # matrix transpose
    tab_trans = [[None] * l for _ in range(c)]

    for i in range(l):
        for j in range(c):
            tab_trans[j][i] = tab[i][j]

    # bubble_sort
    for i in tab_trans:

        for j in range(1, len(i)):
            for k in range(0, len(i) - 1):

                if len(i[j]) > len(i[k]):
                    i[j], i[k] = i[k], i[j]

        mcl.append(len(i[0]))

    line = [[None] * c for _ in range(l)]

    if apart == 0:

        for j in range(l):

            for i in range(c):
                line[j][i] = str(' ' * (mcl[i] - len(tab[j][i])) + tab[j][i] + v)

        for i in range(c):

            for _ in top, bottom, cross_:
                _.append(h * mcl[i])

            top.append(thb)
            bottom.append(bhb)
            cross_.append(cross)

        for x in top, bottom, cross_:
            x.pop()

        print(tlc, *top, trc, sep=b)

        print(v, *line[0], sep=b)

        for i in range(l - 1):
            print(lvb, *cross_, rvb, sep=b)
            print(v, *(line[i + 1]), sep=b)

        print(blc, *bottom, brc, sep=b)

    else:
        separ = s * (c // scale_c)

        for j in range(l):
            for i in range(c):
                line[j][i] = str(v + s * (mcl[i] - len(tab[j][i])) + tab[j][i] + v + s * scale_c)

        for i in range(c):
            top.append(tlc + h * mcl[i] + trc + s * scale_c)
            bottom.append(blc + h * mcl[i] + brc + s * scale_c)

        for i in range(l):

            print(*top, sep=separ)
            print(*line[i], sep=separ)
            print(*bottom, sep=separ)

            for a in range((l // scale_l - 2)):
                print("\n")

    for _ in mcl, top, bottom, cross_:
        _.clear()


print("\n\tInput number of lines, columns of table, their scale, \
sell_split and fill params in format:\n\tx x x x y y; where int(x) >=1, y = 0(False) or 1(True)\n\n\
EXAMPL: 4 5 1 1 0 1\n\
String 1: Прізвище; Ім’я; по-Батькові; дата народження; хобi\n\
String 2: Геррінгтон ;Біллі; Глен Гарольд; 14 липня 1969; SUCK SOME DICK\n\
String 3: Даркхольм; Ван; Некстдоровіч; 24 жовтня 1972; dungeon master & performance artist\n\
String 4: Мілос; Рікардо; Фістович;; FLEX\n ")

table_draw(4, 5, 1, 1, 0, 1, tab)

while True:

    l, c, scale_l, scale_c, apart, fill = list(map(int, input('\nInput: ').split()))

    if fill == 1:
        tab = [[str(i) for i in input('string ' + str(j + 1) + ': ').split(';')] for j in range(l)]

    else:
        tab = [[s] * c for j in range(l)]

    table_draw(l, c, scale_l, scale_c, apart, fill, tab)
