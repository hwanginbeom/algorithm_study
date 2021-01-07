# 요세푸스 문제 0
from collections import deque


# 큐를 사용한 풀이
def solution1() :
    n, k = map(int, input().split())
    q = deque()

    for i in range(1, n + 1) :
        q.append(i)

    answer = []
    while q :
        for _ in range(k - 1) :
            q.append(q.popleft())

        answer.append(q.popleft())

    # 출력
    print('<', end='')

    for i in answer:
        if i == answer[-1]:
            print(i, end='')
        else:
            print(f'{i},', end=' ')

    print('>')


solution1()


# 큐를 사용하지 않은 풀이
def solution2() :
    n, k = map(int, input().split())
    circle = [i for i in range(1, n + 1)]

    answer = []
    cnt = 0

    while circle :
        # 순서가 원형으로 로테이션을 돌도록 로직 구현
        cnt += k

        if cnt % n == 0 :
            cnt = n
        else :
            cnt = cnt % n

        # 인덱스 구하기
        temp = cnt - 1

        answer.append(circle[temp])
        del circle[temp]

        cnt -= 1
        n -= 1

    # 출력
    print('<', end = '')

    for i in answer :
        if i == answer[-1] :
            print(i, end = '')
        else :
            print(f'{i},', end = ' ')

    print('>')


# solution2()
