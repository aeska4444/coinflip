"""
Игра в подбрасывание монетки ака "Ковирская Рулетка".Проигравший удаляет доту
"""
import random
import shutil
import numpy as np

"""
ввести желаемое количество подряд выпавших орлов/решек
"""
n = int(input("streak: "))
"""
создание списка из н единиц
"""
s = [1] * n
"""
Вероятность выпадения события n раз подряд из m попыток
https://www.cyberforum.ru/statistics/thread2041649.html
p/q шанс успеха/неудачи при единичном подбрасывании
однородная цепь Маркова, с матрицей перехода размерностью [n+1]*[n+1],
где n - кол-во нужных удачных результатов. Возводим матрицу в степень m, и смотрим ячейку (0; k+1)
"""
p = 0.5
q = 1 - p
m = n

matrix = np.array(
    [[p] * n + [0]] +
    [[0] * i + [q] + [0] * (n - i) for i in range(n - 1)] +
    [[0] * (n - 1) + [q] + [1]])

matrix_pow = np.linalg.matrix_power(matrix, m)
prob = matrix_pow[n, 0]

while prob < 0.5:
    m += 1
    prob = np.linalg.matrix_power(matrix, m)[n, 0]

"""
подбрасванеи монетки 
"""
flips = [random.randint(0, 1) for i in range(m)]
"""
информация на экран
"""
print(f"probability {prob:.0%} at {m} trows ({int(m * prob)}/{m})")
"""
логическая переменная, глобальное значение номера удачной попытки
"""
flag = False
global num_of_try
"""
проверка в цикле содержит ли список кортежей подбрасываний список единиц;
если да, изменение флага, определение на каком элементе списка это произошло,
выход из цикла
"""
for i in range(len(flips)):

    if flips[i:i + len(s)] == s:
        flag = True
        flips[i:i + len(s)] = chr(9794) * len(s)
        num_of_try = i + 1
        break
"""
процентаж удачливостия, если уложился в отведенные попытки
удаление доты, если неповезло
"""
if flag:
    print(f"Povezlo, povezlo..\n{flips}\t\nluck:\t{(m - len(s)) / num_of_try:.0%}")

else:
    print(f"Better luck next time\n{flips}")

    if not input("Remove Dota Y/N ? ") == ('Y' and 'y'):
        shutil.rmtree('C:/Program Files (x86)/Steam/steamapps/common/dota 2 beta')
