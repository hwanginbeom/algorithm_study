from itertools import combinations as combi


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    # 전체 조합
    candidates = []
    for i in range(1, col + 1):
        candidates.extend(combi(range(col), i))
    # 유일성
    unique = []
    for candi in candidates:
        temp = [tuple(item[i] for i in candi) for item in relation]
        if len(set(temp)) == row:
            unique.append(candi)

    # 최소성
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
    return len(answer)


relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
solution(relation)
