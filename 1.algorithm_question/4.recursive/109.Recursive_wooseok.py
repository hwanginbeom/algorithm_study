# 종이의 개수
# https://www.acmicpc.net/problem/1780
answer_minus = 0
answer_zero = 0
answer_one = 0


# 종이를 9등분하여 반환
def to_nine(paper) :
    n = len(paper)
    big_paper = []

    row_start = 0
    col_start = 0
    row_end = n // 3
    col_end = n // 3

    while row_end <= n :
        normal_paper = []

        for i in range(row_start, row_end) :
            small_paper = []
            for j in range(col_start, col_end) :
                small_paper.append(paper[i][j])

            normal_paper.append(small_paper)

        big_paper.append(normal_paper)

        col_start += n // 3
        col_end += n // 3

        if col_end > n :
            col_start %= n
            col_end %= n

            row_start += n // 3
            row_end += n // 3

    return big_paper


# 종이의 모든 숫자가 같은지 검사
def is_same(paper) :
    global answer_minus, answer_zero, answer_one
    length = len(paper)

    if length == 1 :
        if paper[0][0] == -1 :
            answer_minus += 1
        elif paper[0][0] == 0 :
            answer_zero += 1
        else :
            answer_one += 1
    else :
        num = paper[0][0]
        isSame = True

        for i in range(length) :
            for j in range(length) :
                if num != paper[i][j] :
                    isSame = False
                    break

        if not isSame :
            for new_paper in to_nine(paper):
                is_same(new_paper)
        else :
            if num == -1 :
                answer_minus += 1
            elif num == 0 :
                answer_zero += 1
            else :
                answer_one += 1


def solution() :
    global answer_minus, answer_zero, answer_one
    n = int(input())
    paper = []

    for _ in range(n) :
        temp = list(map(int, input().split()))
        paper.append(temp)

    # print(paper)
    is_same(paper)

    print(answer_minus)
    print(answer_zero)
    print(answer_one)


solution()
