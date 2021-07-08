# 부분합
# https://www.acmicpc.net/problem/1806


def solution() :
    n, s = map(int, input().split())
    num_list = list(map(int, input().split()))

    min_length = 100000000

    for start_index in range(n) :
        sum_value = num_list[start_index]

        # 하나의 요소가 s보다 큰 경우 최소 길이는 1
        if sum_value >= s :
            min_length = 1
            break

        end_index = start_index + 1

        # end_index 부터 더하다가 s 보다 커지거나 끝에 다다르면 탈출
        while sum_value < s and end_index < n :
            sum_value += num_list[end_index]
            end_index += 1

        # 끝까지 더했는데 s 보다 작은 경우 최소를 따질 수 없다.
        if end_index == n :
            if sum_value < s :
                continue

        min_length = min(min_length, end_index - start_index)

    if min_length == 100000000 :
        print(0)
    else :
        print(min_length)


solution()
