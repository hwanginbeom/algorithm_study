# 피로도
# https://programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations


def solution(k, dungeons):
    answer = -1
    entire_list = []

    combi_list = list(permutations(dungeons, len(dungeons)))

    for li in combi_list:
        count = 0
        fatigue = k

        for i in li:
            if fatigue >= i[0]:
                fatigue -= i[1]
                count += 1
            else:
                break

        entire_list.append(count)

    answer = max(entire_list)

    return answer


k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]
print(solution(k, dungeons))
