# 2021-05-21

# 출처 : https://www.acmicpc.net/problem/12015

# 가장 긴 증가하는 부분 수열 2

from bisect import bisect_left

n = int(input())
array = list(map(int, input().split()))

sequence = [array[0]]

for i in array:
    if sequence[-1] < i:
        sequence.append(i)  # 수열의 마지막 값이 리스트에 있는 값보다 작으면 수열에 넣기

    else:
        sequence[bisect_left(sequence, i)] = i

print(len(sequence))