# 1. 구간 합 구하기 4
import sys


def solution1() :
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    valueSum = 0
    intervalSum = [0]

    for a in array :
        valueSum += a
        intervalSum.append(valueSum)

    for _ in range(m) :
        i, j = map(int, sys.stdin.readline().split())
        print(intervalSum[j] - intervalSum[i - 1])


solution1()



# 2. 구간 합 구하기 5
import sys


def solution2() :
    n, m = map(int, input().split())

    array = []
    for _ in range(n) :
        # map(int, input().split())하면 시간 초과 난다....
        temp = list(map(int, sys.stdin.readline().split()))
        array.append(temp)

    # 각 행의 접두사합 구하기
    for i in range(n):
        for j in range(n):
            if j == 0:
                pass
            else:
                array[i][j] += array[i][j - 1]

    for _ in range(m) :
        valueSum = 0
        # 여기도...
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

        for i in range(x1 - 1, x2) :
            if y1 != 1 :
                valueSum -= array[i][y1 - 2]

            valueSum += array[i][y2 - 1]

        print(valueSum)


# solution2()
