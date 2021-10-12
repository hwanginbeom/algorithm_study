# 복서 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/85002


def solution(weights, head2head):
    answer = []
    boxer_info = {}
    n = len(weights)

    for i in range(n):
        entire = 0
        win = 0
        win_big_weight = 0

        # 승률 구하기
        for j in range(len(head2head[i])):
            if head2head[i][j] == 'W':
                entire += 1
                win += 1

                # 자신보다 무거운 복서를 이긴 횟수 구하기
                if weights[i] < weights[j]:
                    win_big_weight += 1
            elif head2head[i][j] == 'L':
                entire += 1

        if entire == 0:
            win_rate = 0
        else:
            win_rate = win / entire

        boxer_info[i + 1] = [win_rate, win_big_weight, weights[i]]

    sorted_list = sorted(boxer_info.items(), key=lambda x: (-x[1][0], -x[1][1], -x[1][2], x[0]))

    for i in sorted_list:
        answer.append(i[0])

    return answer


weights = [50, 82, 75, 120]
head2head = ["NLWL", "WNLL", "LWNW", "WWLN"]
print(solution(weights, head2head))
