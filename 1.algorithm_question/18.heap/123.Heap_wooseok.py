# 가운데를 말해요
# https://www.acmicpc.net/problem/1655
import heapq
import sys # 안쓰면 시간초과


def solution() :
    n = int(sys.stdin.readline())
    left_heap = []
    right_heap = []
    answer = []

    for _ in range(n) :
        num = int(sys.stdin.readline())

        if len(left_heap) == len(right_heap) :
            heapq.heappush(left_heap, (-num, num))
        else :
            heapq.heappush(right_heap, (num, num))
        # print('변경 전 heap : {}, {}'.format(left_heap, right_heap))

        if len(left_heap) >= 1 and len(right_heap) >= 1 and left_heap[0][1] > right_heap[0][1] :
            max_value = heapq.heappop(left_heap)[1]
            min_value = heapq.heappop(right_heap)[1]

            heapq.heappush(left_heap, (-min_value, min_value))
            heapq.heappush(right_heap, (max_value, max_value))

        # print('변경 후 heap : {}, {}'.format(left_heap, right_heap))
        # print()
        answer.append(left_heap[0][1])

    for i in answer :
        print(i)


solution()
