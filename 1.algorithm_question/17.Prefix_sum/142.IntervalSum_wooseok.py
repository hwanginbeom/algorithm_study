# Maximum Subarray
# https://www.acmicpc.net/problem/10211


def solution() :
    t = int(input())
    answer = []

    for _ in range(t) :
        n = int(input())
        num_list = list(map(int, input().split()))

        interval_sum = [0]
        total = 0
        for i in num_list :
            total += i
            interval_sum.append(total)

        max_value = -1000000
        for i in range(1, n + 1) :
            for j in range(i) :
                temp = interval_sum[i] - interval_sum[j]
                max_value = max(max_value, temp)

        answer.append(max_value)

    for i in answer :
        print(i)


solution()
