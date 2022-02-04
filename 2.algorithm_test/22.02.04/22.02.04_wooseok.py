# 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889


def solution(N, stages):
    answer = []

    user_num = len(stages)
    success_dict = {}
    in_stage = 0

    for i in range(1, N + 1):
        sum_value = 0

        for stage in stages :
            if stage >= i :
                sum_value += 1

        in_stage = stages.count(i)

        if sum_value != 0 :
            success_dict[i] = in_stage / sum_value
        else :
            success_dict[i] = 0

    sorted_list = sorted(success_dict.items(), key = lambda x : -x[1])

    for i in sorted_list :
        answer.append(i[0])

    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
