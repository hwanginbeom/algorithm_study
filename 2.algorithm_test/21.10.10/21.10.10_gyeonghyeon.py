import heapq

def solution(cacheSize, cities):
    cities = [ i.lower() for i in cities]
    cache = []
    answer = 0
    for i in cities:
        if i not in cache:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(i)
            else:
                try:
                    cache.pop(0)
                    cache.append(i)
                except:
                    pass
        else:
            answer += 1
            cache.pop(cache.index(i))
            cache.append(i)
    return answer


cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
solution(cacheSize, cities)
