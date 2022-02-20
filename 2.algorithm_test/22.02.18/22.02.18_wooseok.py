import re


def calc_pow(n, op) :
    if op == 'S' :
        return int(n) ** 1
    elif op == 'D' :
        return int(n) ** 2
    elif op == 'T' :
        return int(n) ** 3


def solution(dartResult):
    answer = 0

    score_list = re.findall('[0-9]+', dartResult)
    bonus_list = re.findall('[^0-9]+', dartResult)

    for i in range(3):
        if len(bonus_list[i]) == 2:
            score_list[i] = calc_pow(score_list[i], bonus_list[i][0])

            if bonus_list[i][1] == '*' :
                score_list[i] *= 2
                if i > 0 :
                    score_list[i - 1] *= 2
            else :
                score_list[i] *= -1
        else:
            score_list[i] = calc_pow(score_list[i], bonus_list[i])

    answer = sum(score_list)

    return answer


dartResult = '1S2D*3T'
print(solution(dartResult))
