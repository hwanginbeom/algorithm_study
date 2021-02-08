import sys
input = sys.stdin.readline
from collections import deque


def rtod(r_count, queue) :
    if r_count % 2 == 0 : #짝수
        queue.popleft()
    else : #홀수
        queue.pop()
    return queue

def AC(num_list) :
    r_count = 0
    queue = num_list

    for i in p :
        if i == "R" :
            r_count += 1
        elif i == "D" :
            if len(queue) == 0 :
                answer = 'error'
                return answer
                continue
            else :
                queue = rtod(r_count, queue)

    if r_count % 2 == 1 : #짝수
        queue.reverse()
    # 와... 이 결과 값... 문자형인거 진짜 소름
    answer = "[" + (','.join(map(str,queue))) + "]"
    return answer


t = int(input())
for _ in range(t) :
    p = list(input())
    n = int(input())
    num_list = input()
    num_list = num_list.replace('[','').replace(']','').replace(',',' ')
    num_list = deque(list(map(int, num_list.split())))
    print(AC(num_list))
