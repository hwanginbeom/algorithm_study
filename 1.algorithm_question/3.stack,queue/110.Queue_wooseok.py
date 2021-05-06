# 풍선 터뜨리기
# https://www.acmicpc.net/problem/2346
from collections import deque


def solution() :
    n = int(input())
    balloon_list = list(map(int, input().split()))

    _list = []
    for i in range(len(balloon_list)) :
        _list.append([i + 1, balloon_list[i]])

    queue = deque(_list)
    answer = []

    while True :
        li = queue.popleft()
        answer.append(li[0]) # 풍선 번호

        num = li[1] # 풍선에 있는 종이의 숫자

        if not queue :
            break

        if num > 0 :
            for _ in range(num - 1) :
                queue.append(queue.popleft())
        else :
            for _ in range(abs(num)) :
                queue.appendleft(queue.pop())

    # print(answer)
    for i in answer :
        print(i, end = ' ')


solution()
