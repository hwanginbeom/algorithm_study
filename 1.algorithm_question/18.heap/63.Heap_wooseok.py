# 카드 정렬하기
import heapq, sys


def solution() :
    n = int(sys.stdin.readline())
    q = []

    for _ in range(n) :
        m = int(sys.stdin.readline())
        heapq.heappush(q, m)

    count = 0
    while True :
        if len(q) >= 2 :
            card1 = heapq.heappop(q)
            card2 = heapq.heappop(q)

            sum_card = card1 + card2
            count += sum_card

            if not q :
                break
            else :
                # 최소 힙으로 값을 넣는 이유
                # 뽑은 두 카드묶음을 비교한 횟수가 큐 맨앞의 카드 묶음의 수보다 적으면
                # 더 앞에 배치가 되야 효율적인 비교가 가능해진다. (그리디)
                heapq.heappush(q, sum_card)
        # 처음부터 카드 묶음의 개수가 1개일 경우
        # 비교를 할 필요가 없으므로 비교횟수는 0이 된다.
        else :
            break

    print(count)


solution()
