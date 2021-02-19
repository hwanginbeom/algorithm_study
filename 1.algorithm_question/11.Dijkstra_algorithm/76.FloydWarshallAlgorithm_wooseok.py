# 맥주 마시면서 걸어가기
def solution() :
    t = int(input())
    answer = []

    for _ in range(t) :
        n = int(input())
        node_count = n + 2

        position = []
        for _ in range(node_count) :
            position.append(list(map(int, input().split())))

        graph = [[int(1e9)] * (node_count + 1) for _ in range(node_count + 1)]

        for i in range(node_count) :
            for j in range(node_count) :
                if i == j :
                    graph[i][j] = 0
                    continue

                x_diff = abs(position[j][0] - position[i][0])
                y_diff = abs(position[j][1] - position[i][1])
                d = x_diff + y_diff

                # 맥주 20병으로 갈 수 있는 거리이면
                # 갈 수 있다는 의미로 1 저장
                if d <= 1000 :
                    graph[i][j] = 1

        for k in range(n + 2):
            for a in range(n + 2):
                for b in range(n + 2):
                    graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

        if 0 <= graph[0][n + 1] < int(1e9) :
            answer.append('happy')
        else :
            answer.append('sad')

    for i in answer :
        print(i)


solution()
