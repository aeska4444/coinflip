from random import randrange


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = -1  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]

    def init(self):
        for row in self.pole:
            for i in row:
                i.value = 0

    def show(self):
        print()
        [print(*i) for i in self.pole]
        print()

    def __check(self, args):
        if any(type(i) != int or i not in range(3) for i in args):
            raise IndexError('некорректно указанные индексы')
        return args[0], args[1]

    def human_go(self):
        r, c = self.__check(list(map(int, input("Put coords of free sell: row column\t").split())))
        if self.pole[r][c]:
            self.pole[r][c].value = self.HUMAN_X
        else:
            print("Sell is not empty, choose another")
            return self.human_go()

    def computer_go(self):
        r, c = randrange(0, 3), randrange(0, 3)
        if self.pole[r][c]:
            self.pole[r][c].value = self.COMPUTER_O
        else:
            return self.computer_go()

    def __getitem__(self, item):
        r, c = self.__check(item)
        return self.pole[r][c].value

    def __setitem__(self, key, value):
        r, c = self.__check(key)
        self.pole[r][c].value = value

    @property
    def is_human_win(self):
        return any(sum(map(lambda a: a.value, row)) == 3 for row in self.pole) or \
               any(sum(map(lambda a: a.value, i)) == 3 for i in zip(*self.pole)) or \
               sum(self.pole[i][i].value for i in range(3)) == 3 or \
               sum(self.pole[i][j].value for j in range(3) for i in range(3) if i + j == 2) == 3

    @property
    def is_computer_win(self):
        return any(sum(map(lambda a: a.value, row)) == -3 for row in self.pole) or \
               any(sum(map(lambda a: a.value, i)) == -3 for i in zip(*self.pole)) or \
               sum(self.pole[i][i].value for i in range(3)) == -3 or \
               sum(self.pole[i][j].value for j in range(3) for i in range(3) if i + j == 2) == -3

    @property
    def is_draw(self):
        return all(not i for row in self.pole for i in row)
        # and not (self.is_human_win or self.is_computer_win)

    def __bool__(self):
        return not (self.is_human_win or self.is_computer_win or self.is_draw)


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return not self.value

    def __str__(self):
        return str(self.value).zfill(2)
        # if self:
        #     return ''
        # return ['\u2573', '\u25ef'][self.value >= 0]


game = TicTacToe()
game.init()
step_game = 0

while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1

game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
