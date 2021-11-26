"""
Вероятность выпадения события n раз подряд из m попыток (монетка)
https://www.cyberforum.ru/statistics/thread2041649.html
"""
import numpy as np
np.set_printoptions(precision=2, linewidth=200, suppress=True)

p = 0.5
q = 1 - p

n = int(input("n = "))
m = int(input("m = "))

matrix = np.array(
      [[p] * n + [0]] +
      [[0] * i + [q] + [0] * (n - i) for i in range(n - 1)] +
      [[0] * (n - 1) + [q] + [1]])

matrix_pow = np.linalg.matrix_power(matrix, m)

print(f"\nProbability {matrix_pow[n, 0]:.0%}")

if input("Show matrix? (Y/N) ") == ('Y' and 'y'):
    if n <= 10:
        print(f"\n{matrix}\n\n{matrix_pow}")
    else:
        print(f"\n{matrix}\n\n{matrix_pow}", file=open('matrix.txt', 'a'))
