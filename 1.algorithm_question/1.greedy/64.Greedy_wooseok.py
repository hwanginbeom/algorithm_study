# 수 묶기
from collections import deque


def solution() :
    n = int(input())

    num_list = []
    q = deque([])

    for _ in range(n) :
        m = int(input())
        num_list.append(m)

    num_list.sort(reverse = True)

    # 큐에 정렬된 리스트를 그대로 삽입
    for i in num_list :
        q.append(i)

    sum_value = 0

    # 양수인 경우
    while True :
        if len(q) >= 2 :
            if q[0] > 1 and q[1] > 1 :
                a = q.popleft()
                b = q.popleft()

                sum_value += a * b
            else :
                break
        else :
            break

    # 0 또는 음수일 경우
    while True :
        if len(q) >= 2 :
            if q[-1] <= 0 and q[-2] <= 0 :
                a = q.pop()
                b = q.pop()

                sum_value += a * b
            else :
                break
        else :
            break

    # 남은 값 처리
    if q :
        sum_value += sum(q)

    print(sum_value)


solution()
