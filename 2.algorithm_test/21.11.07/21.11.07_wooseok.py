# 후보키
# https://programmers.co.kr/learn/courses/30/lessons/42890
# 21.04.11 재풀이
from itertools import combinations


def solution(relation):
    answer = 0

    row = len(relation)
    col = len(relation[0])
    idx_list = [i for i in range(col)]

    # 전체 조합
    # 인덱스 번호로 조합하기
    entire_list = []
    for i in range(1, col + 1) :
        entire_list.extend(combinations(idx_list, i))

    # 유일성
    # 전체 데이터의 크기와 중복을 제거한 데이터의 크기가 맞는지 비교
    unique_list = []
    for idx in entire_list :
        temp = [tuple([item[i] for i in idx]) for item in relation]

        if len(set(temp)) == row :
            unique_list.append(idx)

    # 최소성
    minimal_list = set(unique_list)
    for i in range(len(unique_list)) :
        for j in range(i + 1, len(unique_list)) :
            # 유일성을 가지고 있는 튜플이 다른 튜플에 포함되어 있으면, 제거하는 형식
            if len(unique_list[i]) == len(set(unique_list[i]) & set(unique_list[j])) :
                minimal_list.discard(unique_list[j])

    answer = len(minimal_list)
    return answer


relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
print(solution(relation))
# 실패
