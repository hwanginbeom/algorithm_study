#9주차 전력망
#전선 하나를 끊어서 현재 전력망 네트워크를 2개로 분할하려고함
#이때 두전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞출거임
## BFS와 DFS알고리즘 이해도가 있어야함


from collections import defaultdict, deque


def solution(n, wires):
    def bfs(start, x, y):
        q = deque()
        q.append(start)
        dist[start] = 1
        curr = 0
        cnt = 1
        while q:
            curr = q.popleft()

            for next_num in graph[curr]:
                if curr == x and next_num == y or curr == y and next_num == x:
                    continue

                if not dist[next_num]:
                    dist[next_num] = dist[curr] + 1
                    q.append(next_num)
                    cnt += 1
        return cnt

    answer = 1000000
    graph = defaultdict(list)
    for wire in wires:
        a, b = wire
        graph[a].append(b)
        graph[b].append(a)

    for wire in wires:
        dist = [0] * (n + 1)
        a, b = wire
        temp = []
        for i in range(1, n + 1):
            if not dist[i]:
                max_dist = bfs(i, a, b)
                temp.append(max_dist)
        answer = min(answer, abs(temp[0] - temp[1]))
    return answer