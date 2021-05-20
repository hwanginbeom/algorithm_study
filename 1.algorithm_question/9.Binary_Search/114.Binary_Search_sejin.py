from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))

answer = []
for i in a:
    if len(answer)==0:
        answer.append(i)
    elif answer[-1] < i:
        answer.append(i)
    else:
        answer[bisect_left(answer,i)] = i

print(len(answer))
