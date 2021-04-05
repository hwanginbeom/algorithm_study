# 카카오 코딩테스트
# 캐시
# https://programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    cache = []
    # 대소문자 구분 없애기
    c_upper = [i.upper() for i in cities]
    answer = 0
    for city in c_upper:
        # 캐시 크기가 0일 경우 전부 miss
        if cacheSize == 0:
            answer = len(cities) * 5
            break
        # 캐시에 없는 도시일 경우
        if not city in cache:
            # 캐시 크기보다 현재 캐시가 적을 경우 캐시에 도시 추가 (miss)
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                # 캐시 크기 초과 시 캐시에서 가장 오래된 도시를 빼고 새 도시를 추가
                cache.pop(0)
                cache.append(city)
            # 실행시간에 5 추가
            answer += 5
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            answer += 1
    return answer