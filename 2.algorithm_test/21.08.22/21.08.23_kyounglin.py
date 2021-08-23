# 2021-08-23

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/72411

# 메뉴 리뉴얼

# orders=["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course=[2,3,4]
orders=["XYZ", "XWY", "WXA"]
course=[2,3,4]

from itertools import combinations
from collections import Counter

def solution(orders,course):
    answer=[]
    for i in course:
        menu=[]
        for j in orders:
            for k in list(combinations(sorted(j),i)):
                menu.append(''.join(k))

        for key,value in Counter(menu).items():
            if Counter(menu).most_common()[0][1]==value and value>=2:
                answer.append(key)

    return sorted(answer)

print(solution(orders,course))

