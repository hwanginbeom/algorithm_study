# AC
# https://www.acmicpc.net/problem/10817

from collections import deque
import ast
import sys

def AC(q, cnt) :
    # R의 개수의 홀짝을 활용
    if q:
        if cnt % 2 == 0:
            q.popleft()
        else:
            q.pop()

        return q
    else:
        return 'error'

input = sys.stdin.readline
p = []
array = []
T = int(input())
for _ in range(T):
    p.append(input().strip('\n'))
    n = int(input())
    array.append(deque(ast.literal_eval(input())))

for i in range(T):
    cnt = 0
    for j in p[i]:
        if j == 'R':
            cnt += 1
        else:
            array[i] = AC(array[i], cnt)
            if array[i] == 'error':
                break
    if array[i] != 'error' and cnt % 2 == 1:
        array[i].reverse()

for k in array:
    if k == 'error':
        print(k)
    else:
        print(str(list(k)).replace(" ",""))
