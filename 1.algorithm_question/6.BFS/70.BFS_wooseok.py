# 숨바꼭질
from collections import deque


def solution() :
    n, k = map(int, input().split())

    def bfs(start, k):
        # 큐(Queue) 구현을 위해 deque 라이브러리 사용
        queue = deque([start])
        visited = [0] * 100001

        # 큐가 빌 때까지 반복
        while queue:
            v = queue.popleft()

            if v == k :
                break

            # 다이나믹 프로그래밍
            for i in (v - 1, v + 1, v * 2):
                if i >= 0 and i <= 100000 :
                    if not visited[i]:
                        visited[i] = visited[v] + 1
                        queue.append(i)

        return visited

    time_list = bfs(n, k)

    print(time_list[k])


solution()
