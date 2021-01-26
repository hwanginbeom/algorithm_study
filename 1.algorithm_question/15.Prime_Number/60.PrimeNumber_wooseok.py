# 소수&팰린드롬
import math


def solution() :
    n = int(input())

    while True :
        if n == 1 :
            n += 1
            continue

        isFlag = True

        # 소수 판별
        for i in range(2, int(math.sqrt(n)) + 1):
            # x가 해당 수로 나누어떨어진다면
            if n % i == 0:
                n += 1
                isFlag = False
                break
        else :
            string = str(n)
            cnt = len(string) - 1

            # 팰린드롬(회문) 판단
            for i in range(len(string) // 2) :
                if string[i] != string[cnt] :
                    n += 1
                    isFlag = False
                    break
                else :
                    cnt -= 1

        if isFlag :
            break

    print(n)


solution()
