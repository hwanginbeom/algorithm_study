import sys
import heapq


def sol1655():
    maxq, minq = [], []
    n, *nums = map(int, sys.stdin.read().split())
    answer = []
    for num in nums:
        if not maxq or num <= -maxq[0]:
            heapq.heappush(maxq, -num)
        else:
            heapq.heappush(minq, num)
        diff = len(maxq) - len(minq)
        if diff == 2:
            heapq.heappush(minq, -heapq.heappop(maxq))
            diff = 0
        elif diff == -2:
            heapq.heappush(maxq, -heapq.heappop(minq))
            diff = 0

        answer.append(str(-maxq[0] if diff >= 0 else minq[0]))
    print('\n'.join(answer))


if __name__ == '__main__':
    sol1655()