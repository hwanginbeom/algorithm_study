# 카카오 코딩테스트
# 후보키
# https://programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    # 전체 조합
    # combination 의 변수에 range 형식으로 들어가야함
    # tuple 형태로 extend 되어 리스트를 구성
    candidates = []
    for i in range(1, col + 1):
        candidates.extend(combinations(range(col), i))

    # 유일성
    # 전체 조합에 해당하는 항목들로 비교해서 set 으로 중복 제거하고
    # length 를 비교하여 유일한 조합만 리스트에 담기
    unique = []
    for candi in candidates:
        tmp = [tuple([item[i] for i in candi]) for item in relation]
        if len(set(tmp)) == row:
            unique.append(candi)

    # 최소성
    # 각각의 조합을 다른 모든 조합들과 비교하여 포함되어 있는 조합이면 제거
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
    return len(answer)

example = [["100","ryan","music","2"],
            ["200","apeach","math","2"],
            ["300","tube","computer","3"],
            ["400","con","computer","4"],
            ["500","muzi","music","3"],
            ["600","apeach","music","2"]]

print(solution(example))