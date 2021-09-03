# 소수 단어
# https://www.acmicpc.net/problem/2153
import math


def solution() :
    word = input()
    ascii_sum = 0

    for i in word :
        if i.islower() :
            ascii_sum += ord(i) - 96
        else :
            ascii_sum += ord(i) - 38

    for i in range(2, int(math.sqrt(ascii_sum)) + 1) :
        if ascii_sum % i == 0 :
            answer = 'It is not a prime word.'
            break
    else :
        answer = 'It is a prime word.'

    # 1은 소수라는 문제 조건 적용
    if ascii_sum == 1 :
        answer = 'It is a prime word.'

    print(answer)


solution()
