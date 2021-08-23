from itertools import combinations # 조합을 위한 모듈
from collections import Counter # 등장횟수를 위한 모듈

def solution(orders, course):
    answer = []

    for i in course :
        array = []

        for j in orders :
            j = sorted(j)
            array.extend(list(map(''.join, combinations(j,i))))
        # print(array)

        counter = Counter(array)
        # print(dict(counter))

        if (len(counter) != 0) and (max(counter.values()) != 1) :
            for k in counter :
                # print(k)
                if counter[k] == max(counter.values()) :
                    answer += [''.join(k)]

    answer = sorted(answer)
    return (answer)

print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))
