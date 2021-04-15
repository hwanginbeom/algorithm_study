# N번째 큰 수
# https://www.acmicpc.net/problem/2075
import heapq


def solution() :
    n = int(input())
    queue = []

    for _ in range(n) :
        _list = list(map(int, input().split()))

        # 메모리초과를 해결하기 위해
        # 숫자를 저장할 힙의 길이를 N 으로 한정한다.
        # 힙의 길이가 N 보다 작으면 그냥 push
        # 힙의 길이가 N 보다 크면 push 한 다음, 최솟값을 pop 한다. (순서 매우 중요)
        for i in _list :
            if len(queue) < n :
                heapq.heappush(queue, i)
            else :
                heapq.heappush(queue, i)
                heapq.heappop(queue)

    print(queue[0])


solution()
