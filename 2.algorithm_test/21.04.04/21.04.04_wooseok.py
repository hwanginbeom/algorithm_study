# 캐시
# https://programmers.co.kr/learn/courses/30/lessons/17680
from collections import deque


def solution(cacheSize, cities):
    answer = 0

    cache = deque([])
    cities = [i.lower() for i in cities]

    if cacheSize == 0:
        answer = len(cities) * 5
    else:
        for city in cities:
            # 캐시 안에 데이터가 있는 경우
            if city in cache:
                del cache[cache.index(city)]
                cache.appendleft(city)
                answer += 1
            # 캐시 안에 데이터가 없는 경우
            else:
                if 0 <= len(cache) < cacheSize:
                    cache.appendleft(city)
                    answer += 5
                else:
                    cache.pop()
                    cache.appendleft(city)
                    answer += 5

    return answer


cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities))
