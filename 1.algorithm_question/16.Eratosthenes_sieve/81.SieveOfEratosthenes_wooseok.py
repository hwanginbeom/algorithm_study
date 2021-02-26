# 골드바흐의 추측
import math


def solution() :
    t = int(input())

    for _ in range(t) :
        n = int(input())

        # 에라토스테네스의 체
        array = [True for _ in range(n + 1)]

        for i in range(2, int(math.sqrt(n)) + 1) :
            j = 2

            while i * j <= n :
                array[i * j] = False
                j += 1

        a = n // 2
        b = a

        while True :
            if array[a] and array[b] :
                print(a, end = ' ')
                print(b)
                break
            # 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있는데
            # 딱 반으로 나눈 후, 두 수를 동시에 각각 -1, +1을 해주면
            # 이 두 수가 소수인 경우를 찾는 것과 동일하다.
            else :
                a -= 1
                b += 1


solution()
