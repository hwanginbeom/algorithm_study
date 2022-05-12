# 최대 힙
# https://www.acmicpc.net/problem/11279
import heapq


def solution() :
    n = int(input())
    num_list = []
    answer = []

    for _ in range(n) :
        x = int(input())

        if x == 0 :
            if not num_list :
                answer.append(0)
            else :
                max_item = heapq.heappop(num_list)
                answer.append(max_item[1])
        else :
            heapq.heappush(num_list, (-x, x))

    for i in answer :
        print(i)


solution()
