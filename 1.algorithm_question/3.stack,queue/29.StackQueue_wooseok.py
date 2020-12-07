# 1. 제로
def solution1() :
    k = int(input())
    account = []

    for _ in range(k) :
        n = int(input())

        if n != 0 :
            account.append(n)
        else :
            account.pop()

    print(sum(account))


# solution1()



# 2. 카드2
from collections import deque


def solution2() :
    n = int(input())

    # 단순 list나 queue 자료구조를 사용했을 경우 시간초과 발생...
    # deque 사용
    q = deque([i for i in range(1, n + 1)])

    while True :
        if len(q) == 1 :
            break

        q.popleft()
        if len(q) == 1 :
            break

        q.append(q.popleft())

    print(q.pop())


solution2()
