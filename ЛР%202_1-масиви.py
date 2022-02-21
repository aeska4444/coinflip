import random

size = 10

A = [[random.randint(-10, 10) for i in range(size)] for j in range(size)]
pd = primediagonal = [A[i][i] for i in range(size)]
sd = seconddiagonal = [A[i][-1*(i+1)] for i in range(size)]


def bubble(arr):

    sortedarr = arr
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sortedarr[j] > sortedarr[j + 1]:
                sortedarr[j], sortedarr[j + 1] = sortedarr[j + 1], sortedarr[j]
    return sortedarr


for i in range(size):
    print(*A[i])
#1
print(-bubble(sd)[-1])
#2
count = 0
sum = 0
for i in range(size):
    for j in range(size):
        if A[i][j] < 0:
            count += 1
for i in range(len(pd)):
    sum += pd[i]
print(count, sum)
#3
print(bubble(pd))
