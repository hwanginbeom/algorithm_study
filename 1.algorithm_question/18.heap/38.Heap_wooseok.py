# 더 맵게
import heapq


def solution(scoville, K):
    answer = 0
    q = []

    for s in scoville:
        heapq.heappush(q, s)

    while True:
        if len(q) >= 2:
            a = heapq.heappop(q)
            b = heapq.heappop(q)

            heapq.heappush(q, a + b * 2)

            answer += 1

            if q[0] >= K:
                break
        # 큐 안에 원소가 하나밖에 안남았을 경우
        else:
            if q[0] >= K:
                break
            else:
                return -1

    return answer


scoville = [1, 2, 3, 9, 10, 12]
K = 7

print(solution(scoville, K))
