# 교점에 별 만들기
# https://programmers.co.kr/learn/courses/30/lessons/87377


def solution(line):
    answer = []
    points = []
    n = len(line)

    # 값이 정수인 교점 구하기
    for i in range(n):
        for j in range(i + 1, n):
            down = line[i][0] * line[j][1] - line[i][1] * line[j][0]

            if down != 0:
                x_up = line[i][1] * line[j][2] - line[i][2] * line[j][1]
                y_up = line[i][2] * line[j][0] - line[i][0] * line[j][2]
                x, y = x_up / down, y_up / down

                if x == int(x) and y == int(y):
                    points.append([int(x), int(y)])

    # 별을 찍을 전체 좌표 만들기
    converted = list(map(list, zip(*points)))
    max_x, min_x = max(converted[0]), min(converted[0])
    max_y, min_y = max(converted[1]), min(converted[1])
    row = abs(max_x - min_x + 1)
    col = abs(max_y - min_y + 1)

    graph = [['.'] * row for _ in range(col)]

    # 별 찍기
    # 별을 찍을 때는 그래프 안에 있는 점들을 1사분면에 옮긴다 생각
    # 그 이유는 컴퓨터의 2차원 배열이 그래프의 1사분면을 뒤집은 형태로 표현되기 때문
    # y좌표 = max_y - y, x좌표 = x - min_x
    for point in points:
        graph[max_y - point[1]][point[0] - min_x] = '*'

    for i in graph:
        answer.append(''.join(i))

    return answer


line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
print(solution(line))
