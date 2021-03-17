# 회전하는 큐
# https://www.acmicpc.net/problem/1021
from collections import deque


def solution() :
    n, m = map(int, input().split())

    num_list = list(map(int, input().split()))

    q = deque([])
    for i in range(1, n + 1) :
        q.append(i)

    answer = 0
    for i in num_list :
        idx = q.index(i)

        # 왼쪽과 오른쪽 중 횟수가 더 적게 드는 연산 선택
        if idx <= (len(q) // 2) :
            while q[0] != i :
                q.append(q.popleft())
                answer += 1

            q.popleft()
        else :
            while q[0] != i:
                q.appendleft(q.pop())
                answer += 1

            q.popleft()

    print(answer)


solution()
