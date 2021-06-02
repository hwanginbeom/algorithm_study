# 회장뽑기
# https://www.acmicpc.net/problem/2660


def solution() :
    n = int(input())

    graph = [[1e9] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1) :
        for j in range(1, n + 1) :
            if i == j :
                graph[i][j] = 0

    while True :
        a, b = map(int, input().split())

        if a == -1 and b == -1 :
            break

        graph[a][b] = 1
        graph[b][a] = 1

    # 플로이드-와셜 알고리즘
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    _dict = {}

    # 회원번호와 점수를 저장
    for i in range(1, n + 1) :
        temp = graph[i][1:]
        _dict[i] = max(temp)

    # 정렬하여 가장 낮은 점수 구하기
    sorted_list = sorted(_dict.items(), key = lambda x : x[1])
    _max = sorted_list[0][1]

    count = 0
    max_list = []

    # 가장 낮은 점수인 회원 구하기
    for i in sorted_list :
        if i[1] == _max :
            count += 1
            max_list.append(i[0])
        else :
            break

    print(_max, count)
    for i in max_list :
        print(i, end = ' ')


solution()
