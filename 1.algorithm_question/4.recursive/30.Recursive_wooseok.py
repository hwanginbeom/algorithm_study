# 팩토리얼
def solution1() :
    n = int(input())
    result = 1

    for i in range(1, n + 1) :
        result *= i

    print(result)


# solution1()


def recursive(n) :
    if n == 1 or n == 0 :
        return 1
    return n * recursive(n - 1)


def solution2() :
    n = int(input())
    print(recursive(n))


solution2()
