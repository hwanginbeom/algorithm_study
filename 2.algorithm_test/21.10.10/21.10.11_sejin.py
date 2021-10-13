def solution(cacheSize, cities):
    cache = []
    answer = 0

    for i in cities:
        i = i.lower()

        # cashesize가 0이면 *5
        if cacheSize == 0:
            answer = len(cities) * 5
            break

        # cache hit
        # cache에 해당 도시 있다면, 그 인덱스 없애고 뒤로 붙이기
        if i in cache:
            cache.pop(cache.index(i))
            cache.append(i)
            answer += 1

        # cache miss
        # cache에 해당 도시 없다면, 뒤로 붙이기
        else:
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(i)
            answer += 5

    return answer