# 합 구하기
def solution() :
    n = int(input())
    n_list = list(map(int, input().split()))

    sum_value = 0
    prefix_sum = [0]

    # 접두사 합 구하기
    # 첫번째 수 부터 i 까지의 합
    for i in n_list :
        sum_value += i
        prefix_sum.append(sum_value)

    m = int(input())
    answer = []

    for _ in range(m) :
        a, b = map(int, input().split())
        answer.append(prefix_sum[b] - prefix_sum[a - 1])

    for i in answer :
        print(i)


solution()
