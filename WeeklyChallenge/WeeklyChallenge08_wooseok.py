# 최소직사각형
# https://programmers.co.kr/learn/courses/30/lessons/86491


def solution(sizes):
    answer = 0

    max_length = 0
    max_width = 0

    for size in sizes:
        if size[0] < size[1]:
            size.reverse()

        max_length = max(max_length, size[0])
        max_width = max(max_width, size[1])

    answer = max_length * max_width

    return answer


sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))
