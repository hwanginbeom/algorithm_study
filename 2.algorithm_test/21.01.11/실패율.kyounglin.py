# 2021-01-11 coding test

# 실패율

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/42889


def solution(N, stages):
    answer = []
    n = len(stages)

    for i in range(1, N + 1):
        cnt = stages.count(i)
        if cnt == 0:
            per = 0

        else:
            per = cnt / n

        answer.append((i, per))
        n -= cnt

    answer.sort(key=lambda x: -x[1])
    answer = [x for x, y in answer]

    return answer