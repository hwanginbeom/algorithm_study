# 과제는 끝나지 않아!
# https://www.acmicpc.net/problem/17952


def solution() :
    n = int(input())

    assign_list = []
    answer = 0

    for _ in range(n) :
        string = input()

        # 점수와 걸리는 시간 저장
        if string != '0' :
            string_split = string.split()
            assign_list.append([int(string_split[1]), int(string_split[2])])

        # 반복을 돌 때마다 제일 최신과제의 걸리는 시간 -1
        if assign_list :
            assign_list[-1][1] -= 1

            if assign_list[-1][1] == 0 :
                assign = assign_list.pop()
                answer += assign[0]

    print(answer)


solution()
