import heapq
def numnum(x1,x2):
    result = x1 + (x2 * 2)
    return result


def solution(scoville, K):
    h = []
    answer = 0
    for i in scoville:
        heapq.heappush(h, i)
    while h:
        num1 = heapq.heappop(h)
        num2 = heapq.heappop(h)
        num3 = numnum(num1,num2)
        heapq.heappush(h, num3)
        answer +=1
        if h[0] >= K or len(h) == 1:
            break
    if h[-1] < K:
        answer = -1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))