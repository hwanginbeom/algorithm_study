import math

n = 1000000
array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1


def solution():
    n, m = map(int, input().split())
    num_list = [i for i in range(2, m + 1) if array[i]]
    answer = [str(i) for i in num_list if n <= i <= m]
    print('\n'.join(answer))

solution()
