# 후보키
# https://programmers.co.kr/learn/courses/30/lessons/42890
from itertools import combinations


def solution(relation):
    answer = 0

    row = len(relation)
    col = len(relation[0])

    # 전체 조합
    all_candi_list = []
    for i in range(1, col + 1) :
        all_candi_list.extend(combinations(range(col), i))

    # 유일성
    unique_list = []
    for candi in all_candi_list :
        temp = [tuple([item[i] for i in candi]) for item in relation]

        if len(set(temp)) == row :
            unique_list.append(candi)

    # 최소성
    answer = set(unique_list)
    for i in range(len(unique_list)) :
        for j in range(i + 1, len(unique_list)) :
            # 최소성을 구하는 로직
            # 유일성을 가지고 있는 튜플이 다른 튜플에 포함되어 있으면, 제거하는 형식
            if len(unique_list[i]) == len(set(unique_list[i]) & set(unique_list[j])) :
                answer.discard(unique_list[j])

    return len(answer)


relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
print(solution(relation))
