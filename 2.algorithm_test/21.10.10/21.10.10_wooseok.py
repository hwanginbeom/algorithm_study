# 캐시
# https://programmers.co.kr/learn/courses/30/lessons/17680
# 21.04.04 재풀이


def solution(cacheSize, cities):
    answer = 0

    cache = []
    for city in cities:
        city = city.lower()

        if city in cache:
            del cache[cache.index(city)]
            cache.append(city)
            answer += 1
        else:
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                if cacheSize > 0:
                    del cache[0]
                    cache.append(city)
            answer += 5

    return answer


cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities))
