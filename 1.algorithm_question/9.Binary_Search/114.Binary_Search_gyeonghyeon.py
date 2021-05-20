import sys
input = sys.stdin.readline


def lower_bound(arr, start, end, n):
    while start < end:
        mid = (start + end) // 2

        if arr[mid] < n:
            start = mid + 1
        else:
            end = mid
    return end

n = int(input())
a = list(map(int, input().split()))

answer = []
for num in a:
    if len(answer) == 0:
        answer.append(num)

    if answer[-1] < num:
        answer.append(num)
    else:
        idx = lower_bound(answer,0,len(answer)-1,num)
        answer[idx] = num

print(len(answer))