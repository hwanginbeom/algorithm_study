import numpy as np


def get_score(i):
    final_score = ''
    if i >= 90:
        final_score += 'A'
    elif 80 <= i < 90:
        final_score += 'B'
    elif 70 <= i < 80:
        final_score += 'C'
    elif 50 <= i < 70:
        final_score += 'D'
    else:
        final_score += 'F'
    return final_score


def solution(scores):
    answer = ''
    for idx, score in enumerate(list(map(list, zip(*scores)))):
        max_num, min_num = max(score), min(score)
        if score[idx] == max_num and score.count(max_num) == 1:
            score.remove(max_num)
        elif score[idx] == min_num and score.count(min_num) == 1:
            score.remove(min_num)
        answer += get_score(np.mean(score))
    return answer


scores = [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65],
          [24, 90, 94, 75, 65]]
solution(scores)
