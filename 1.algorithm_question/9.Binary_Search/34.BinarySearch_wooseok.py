# 공유기 설치
def solution() :
    n, c = map(int, input().split())
    house = []

    for _ in range(n) :
        house.append(int(input()))

    house.sort()

    start = 1
    end = house[-1] - house[0]

    result = 0

    while start <= end :
        # 초기 간격 설정
        mid = (start + end) // 2

        # 첫 집
        old = house[0]

        # 첫 집에 공유기 설치
        count = 1

        for i in range(1, len(house)) :
            # 첫 집과 특정 간격(mid) 이상 떨어져 있는 제일 가까운 집을 구하는 과정
            if house[i] >= old + mid :
                count += 1
                old = house[i]

        # 설치한 공유기의 개수가 주어진 개수보다 많으면
        if count >= c :
            # 간격을 늘려서 배치해보기 (공유기 수를 줄이기 위해)
            start = mid + 1
            result = mid
        # 설치한 공유기의 개수가 주어진 개수보다 적으면
        else :
            # 간격을 줄여서 배치해보기 (공유기의 수를 늘이기 위해)
            end = mid - 1

    print(result)


solution()
