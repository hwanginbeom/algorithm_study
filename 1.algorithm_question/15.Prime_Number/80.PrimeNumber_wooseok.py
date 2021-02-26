# 소수 부분 문자열
import math


def is_prime_number(x) :
    for i in range(2, int(math.sqrt(x)) + 1) :
        if x % i == 0 :
            return False

    return True


def solution() :
    prime_list = []

    while True :
        n = input()

        if n != '0' :
            prime_list.append(n)
        else :
            break

    answer = []

    for p in prime_list :
        _max = 0

        # 최대 6자리까지 지정하여 완전탐색으로 모든 경우를 판별
        for i in range(len(p)) :
            for j in range(i + 1, i + 6) :
                if j <= len(p) :
                    num = int(p[i:j])

                if 2 <= num <= 100000 :
                    flag = is_prime_number(num)

                    if flag :
                        _max = max(_max, num)

        answer.append(_max)

    for i in answer :
        print(i)


solution()
