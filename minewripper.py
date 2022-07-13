from random import sample


class Cell:
    def __init__(self, mine):
        self.mine = mine
        self.around_mines = 0
        self.fl_open = True

    def show(self):
        if not self.fl_open:
            return '#'
        elif self.mine:
            return '*'
        return self.around_mines


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = self.init()
        for i in sample(range(N * N), M):
            self.pole[i // N][i % N] = Cell(1)

    def init(self):
        return [[Cell(0) for _ in range(self.N)] for _ in range(self.N)]

    def show(self):
        n = [-1, 0, 1]
        for i in range(self.N):
            for j in range(self.N):
                self.pole[i][j].around_mines = \
                    sum([self.pole[i + k][j + l].mine
                         for k in n for l in n if i + k in range(0, self.N) and j + l in range(0, self.N)])
                print(self.pole[i][j].show(), end=' ')
            print()


pole_game = GamePole(10, 12)
pole_game.show()
pole_game1 = GamePole(5, 15)
pole_game1.show()
