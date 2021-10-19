# 순위검색
# https://programmers.co.kr/learn/courses/30/lessons/72412
# 21.02.15 재풀이
from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []
    info_dict = {}

    for i in range(len(info)):
        split_list = info[i].split()

        prefer = split_list[:-1]
        score = split_list[-1]

        # 가질 수 있는 모든 선호목록(점수를 뺀 나머지 요소)들의 조합으로 딕셔너리 생성
        for j in range(5) :
            for k in combinations(prefer, j) :
                temp = ''.join(k)

                if temp in info_dict :
                    info_dict[temp].append(int(score))
                else :
                    info_dict[temp] = [int(score)]

    # 딕셔너리 값 내부의 점수들을 정렬
    for i in info_dict :
        info_dict[i].sort()

    for q in query :
        split_list = q.split(' ')

        prefer = split_list[:-1]
        score = split_list[-1]

        # and 와 - 를 제거
        while 'and' in prefer :
            prefer.remove('and')

        while '-' in prefer :
            prefer.remove('-')

        temp = ''.join(prefer)

        if temp in info_dict.keys() :
            scores = info_dict[temp]

            # 선호기준을 만족하는 리스트에서 특정 점수 이상인 것의 개수 계산
            if scores :
                enter = bisect_left(scores, int(score))
                answer.append(len(scores) - enter)
        else:
            answer.append(0)

    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
print(solution(info, query))
# 실패
