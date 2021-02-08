# AC
import re
from collections import deque


def d_func(q, cnt) :
    # R의 개수의 홀짝을 활용
    if q :
        if cnt % 2 == 0 :
            q.popleft()
        else :
            q.pop()

        return q
    else :
        return 'error'


def solution() :
    t = int(input())
    answer = []

    for _ in range(t) :
        func = list(input())
        n = int(input())
        li = input()

        li = re.findall('\d+', li)
        q = deque(li)

        cnt = 0

        for f in func :
            # R(reverse)가 나오면
            # 나올 때마다 reverse 하면 매우 비효율적...
            # R의 개수 활용
            if f == 'R' :
                cnt += 1
            else :
                q = d_func(q, cnt)

                if q == 'error' :
                    answer.append(q)
                    break

        # 출력형태로 변형
        if q != 'error' :
            if cnt % 2 == 1 :
                q.reverse()

            str = '['

            for index, value in enumerate(q) :
                if index == len(q) - 1 :
                    str += value
                else :
                    str += value + ','

            str += ']'

            answer.append(str)

    for i in answer :
        print(i)


solution()
