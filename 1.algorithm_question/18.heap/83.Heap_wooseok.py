# 절댓값 힙
import heapq


def solution() :
    n = int(input())

    oper_list = []
    q = []

    for _ in range(n) :
        oper_list.append(int(input()))

    answer = []

    for o in oper_list :
        if o != 0 :
            # 튜플 활용
            heapq.heappush(q, (abs(o), o))
        else :
            if not q :
                answer.append((0, 0))
            else :
                answer.append(heapq.heappop(q))

    for i in answer :
        print(i[1])


solution()
