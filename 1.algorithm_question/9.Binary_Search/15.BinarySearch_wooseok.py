# 1
def solution1():
    k, n = map(int, input().split())

    lan = []
    for _ in range(k):
        lan.append(int(input()))

    start = 1
    end = max(lan)

    # 적절한 랜선의 길이를 찾는 알고리즘
    while start <= end :
        mid = (start + end) // 2
        lines = 0

        for i in lan :
            lines += i // mid  # 분할된 랜선 수

        if lines >= n :
            start = mid + 1
        else :
            end = mid - 1

    print(end)


solution1()



# 2
def solution2():
    n, m = map(int, input().split())

    tree = list(map(int, input().split()))

    start = 0

    # 끝을 리스트에서 가장 큰 값으로 잡아준다.
    end = max(tree)

    result = 0

    while start <= end:
        total = 0
        mid = (start + end) // 2

        # 중간값보다 나무의 길이가 큰 경우에만 빼서 남은 길이를 더해준다.
        for i in tree:
            if i > mid:
                total += i - mid

        # 나무를 왼쪽 선을 시작으로 늘어놓았을 경우
        # --------------
        # --------
        # -------------------
        # -----------
        # 자르고 남은 길이의 합이 원하는 값보다 낮으면
        # 남는 길이가 더 길도록 잘라야 하므로 범위를 왼쪽으로 좁힌다.
        if total < m:
            end = mid - 1
        # 자르고 남은 길이의 합이 원하는 값보다 크면
        # 일단 값을 결과에 저장하고, 더 짧게 잘라도 되므로
        # 범위를 오른쪽으로 좁힌다.
        else:
            result = mid
            start = mid + 1

    print(result)


# solution2()
