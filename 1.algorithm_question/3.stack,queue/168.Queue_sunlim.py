#백준 13417번
#카드 문자열


from sys import stdin
from collections import deque


T = int(stdin.readline())

for _ in range(T):
    res_list = []
    N = int(stdin.readline())
    card_list = deque(stdin.readline().split())
    res_list.append(card_list.popleft())
    while card_list:
        tmp = card_list.popleft()
        if tmp > res_list[0]:
            res_list.append(tmp)
        else:
            res_list.insert(0,tmp)
    print(''.join(res_list))




