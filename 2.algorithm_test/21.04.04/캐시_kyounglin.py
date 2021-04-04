# 2021-04-04

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/17680?language=python3

# 캐시

cacheSize=3
#cities=["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
cities=["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]


def solution(cacheSize,cities):
    cities = [i.lower() for i in cities]  # 대소문자 구별을 없애기 위해 소문자로 변경
    time = 0 # 실행시간 기록
    cache=[] # 도시를 담을 리스트? 캐시 저장소?

    if cacheSize==0: # 캐시크기가 0이면 캐시에 그냥? 넣어줌 데이터 제거도 필요 없음
        time+=len(cities)*5
    else: #캐시크기가 정해져 있는 경우
        for city in cities: # 도시를 하나씩 불러옴
            if city in cache: # cache hit - 존재하는 데이터가 들어온 경우
                cache.pop(cache.index(city)) # 해당 데이터 꺼내기
                cache.append(city) # 가장 최근 데이터 위치로 보내줌
                time+=1 # cache hit 이므로 시간 +1
            else: # cache miss인 경우
                if len(cache)<cacheSize: #캐시가 꽉 차지 않은 경우
                    cache.append(city) # 그냥 캐시에 넣어주기
                    time+=5 # cahce miss이므로 +5
                else:
                    cache.pop(0) # 꽉 찼을경우 가장 오래된 데이터 제거
                    cache.append(city) # 가장 최근 데이터 위치로 보내줌
                    time+=5 # cahce miss이므로 +5

    return time

print(solution(cacheSize,cities))