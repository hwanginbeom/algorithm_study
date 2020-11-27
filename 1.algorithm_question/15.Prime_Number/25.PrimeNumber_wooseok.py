# 1. 베르트랑 공준
import math


def is_prime_number1(n) :
    count = 0

    for i in range(n + 1, 2 * n + 1) :
        isFlag = True

        for j in range(2, int(math.sqrt(i)) + 1) :
            if i % j == 0 :
                isFlag = False
                break

        if isFlag :
            count += 1

    return count


def solution1() :
    while True :
        n = int(input())

        if n == 0 :
            break
        else :
            print(is_prime_number1(n))


# solution1()



# 2. 소수
import math


def is_prime_number2(m, n) :
    prime_list = []

    for i in range(m, n + 1):
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else :
            if i != 1 :
                prime_list.append(i)

    return prime_list


def solution2() :
    m = int(input())
    n = int(input())

    prime_list = is_prime_number2(m, n)

    if len(prime_list) == 0:
        print('-1')
    else :
        print(sum(prime_list))
        print(min(prime_list))


solution2()
