# 프로그래머스 heap 더 맵게
import heapq

def solution(scoville, k):
    heapq.heapify(scoville)
    count = 0
    while(1):

        if scoville[0] <= k:
            if len(scoville) == 1:
                count = -1
                break
            one = heapq.heappop(scoville)
            two = heapq.heappop(scoville)
            new = one + (two *2)
            heapq.heappush(scoville, new)
            count += 1
        else:
            break
    print(count)
    answer = count
    return answer


scoville = [1, 1, 100]
k = 7
solution(scoville, k)