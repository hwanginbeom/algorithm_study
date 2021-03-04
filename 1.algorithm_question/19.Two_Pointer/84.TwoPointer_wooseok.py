# 두 수의 합
def solution() :
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())

    arr.sort()

    a = 0
    b = len(arr) - 1
    count = 0

    while a != b :
        sum_value = arr[a] + arr[b]

        if sum_value == x :
            count += 1
            b -= 1
        elif sum_value > x :
            b -= 1
        else :
            a += 1

    print(count)


solution()
