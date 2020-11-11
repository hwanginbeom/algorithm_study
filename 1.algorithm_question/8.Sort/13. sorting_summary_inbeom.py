#2217 로프 ( sort)
import sys
input = sys.stdin.readline

N = int(input())
result = []
for i in range(N):
    result.append(int(input()))
result.sort(reverse=True)

max_value = 0
for i in range(len(result)):
    temp = result[i] * (i+1)
    if temp > max_value:
        max_value = temp
print(max_value)



# 1931 회의실 배정
import sys

input = sys.stdin.readline

room = []
for i in range(int(input())):
    a, b = map(int, input().split(' '))
    room.append([a, b])

room = sorted(room, key=lambda x: (x[1], x[0]))
before = room[0][1]
cnt = 1
for i in room[1:]:
    start, end = i[0], i[1]
    if start >= before:
        cnt += 1
        before = end
print(cnt)