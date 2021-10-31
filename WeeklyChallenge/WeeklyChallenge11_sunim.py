import heapq
from collections import deque


def solution(healths, items):
    # 플레이어 체력 오름차순으로 정
    healths.sort()
    items = [(*item, idx) for idx, item in enumerate(items, 1)]
    items.sort(key=lambda x: x[1])  # 1) 피해 기준 오름차
    items = deque(items)
    # print(items)

    candidate = []
    result_list = []

    for player in healths:
        # print(items[1])
        while items and player - items[0][1] >= 100:
            item = items.popleft()  # 지금 쓸수 잇는 아이
            heapq.heappush(candidate, (-item[0], item[2]))  # 아이템 공격력 큰게 가장 앞에 가도록
        if candidate:
            big_idx = heapq.heappop(candidate)[1]  # 담긴 애들중 가장 큰놈을 꺼내
            result_list.append(big_idx)  # 해당 인덱스 넣어주기

    result_list.sort()
    return result_list