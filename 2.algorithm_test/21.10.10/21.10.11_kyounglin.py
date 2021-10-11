# 2021-10-11

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/17680

# 캐시

cacheSize=3
cities=["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

def solution(cacheSize,cities):
    cities = [i.lower() for i in cities]
    time = 0
    cache=[]

    if cacheSize==0:
        time+=len(cities)*5
    else:
        for city in cities:
            if city in cache: # cache hit
                cache.pop(cache.index(city))
                cache.append(city)
                time+=1
            else: # cache miss
                if len(cache)<cacheSize:
                    cache.append(city)
                    time+=5
                else: # 캐시가 꽉 찬 경우
                    cache.pop(0)
                    cache.append(city)
                    time+=5

    return time

print(solution(cacheSize,cities))