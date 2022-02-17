# 강의실 배정
# https://www.acmicpc.net/problem/11000
import heapq


def solution() :
    n = int(input())
    class_list = []

    for _ in range(n) :
        a = list(map(int, input().split()))
        class_list.append(a)

    class_list.sort()
    classroom = [class_list[0][1]]

    for i in range(1, n) :
        if classroom[0] > class_list[i][0] :
            heapq.heappush(classroom, class_list[i][1])
        else :
            heapq.heappop(classroom)
            heapq.heappush(classroom, class_list[i][1])

    print(len(classroom))


solution()
