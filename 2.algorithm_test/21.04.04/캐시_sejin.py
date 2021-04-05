# LRU 알고리즘
# CACHE MISS : 새로운 데이터가 들어온 경우
# 1. 캐시에 넣어준다
# 2. 캐시가 가득차있다면, 가장 오래된 데이터를 제거하고 넣어준다
# CACHE HIT : 존재하는 데이터가 들어온 경우
# 1. 해당 데이터를 꺼낸다
# 2. 가장 최근 데이터 위치로 보내준다

cashesize = 2
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]

cache = []
answer = 0

for i in cities:
    i = i.lower()

    if cashesize == 0:
        answer = len(cities) * 5
        break

    # cache hit : cache 안에 있다
    # len 찼던 안찼던 우선 그 수 pop하고 append
    if i in cache:
        cache.pop(cache.index(i))
        cache.append(i)
        answer += 1

    # cache miss : cache 안에 없다
    # len 안찼으면 그냥 append, 찼으면 앞에서 pop하고 append
    else:
        if len(cache) == cashesize:
            cache.pop(0)
        cache.append(i)
        answer += 5

print(answer)


# 첫번째 오류난 케이스
# 길이로 먼저 조건문 하니까 같은 글자가 들어올 때 len 다 안채워졌을때 문제가 생겼다