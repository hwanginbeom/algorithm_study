# 상호 평가
# https://programmers.co.kr/learn/courses/30/lessons/83201


def divide_score(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'


def solution(scores):
    answer = ''
    n = len(scores)

    # 행렬 전환
    scores = list(map(list, zip(*scores)))

    for i in range(n):
        max_score = max(scores[i])
        min_score = min(scores[i])

        # 자신에게 준 점수가 최고점일 경우
        if scores[i][i] == max_score:
            if scores[i].count(max_score) == 1:
                avg_score = (sum(scores[i]) - scores[i][i]) / (n - 1)
            else:
                avg_score = sum(scores[i]) / n
        # 최저점일 경우
        elif scores[i][i] == min_score:
            if scores[i].count(min_score) == 1:
                avg_score = (sum(scores[i]) - scores[i][i]) / (n - 1)
            else:
                avg_score = sum(scores[i]) / n
        else:
            avg_score = sum(scores[i]) / n

        answer += divide_score(avg_score)

    return answer


scores = [[70, 49, 90], [68, 50, 38], [73, 31, 100]]
print(solution(scores))
