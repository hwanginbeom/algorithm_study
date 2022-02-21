import sys, heapq

input = sys.stdin.readline


def solution():
    answer = []
    n = int(input())
    lecture = [list(map(int, input().split())) for _ in range(n)]
    lecture.sort(key=lambda x: x[0])
    heapq.heappush(answer, lecture[0][1])
    for i in range(1, n):
        start_time = lecture[i][0]
        end_time = lecture[i][1]
        if answer[0] > start_time:
            heapq.heappush(answer, end_time)
        else:
            heapq.heappop(answer)
            heapq.heappush(answer, end_time)
    print(len(answer))
    return answer


solution()
