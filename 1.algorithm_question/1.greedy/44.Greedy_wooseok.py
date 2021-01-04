# ATM
def solution() :
    n = int(input())
    p = list(map(int, input().split()))

    p.sort()
    sum_list = [0] * (n + 1)

    # 접두사 합
    for i in range(n) :
        sum_list[i + 1] = sum_list[i] + p[i]

    print(sum(sum_list))


solution()
