# 2021-09-26

# 출처  : https://programmers.co.kr/learn/courses/30/lessons/64065

# 튜플

s="{{2},{2,1},{2,1,3},{2,1,3,4}}"

import re

def solution(s):
    array=[re.findall('\d+',i) for i in s.split('},')]

    answer=[]

    for j in sorted(array,key=len):
        for k in j:
            if int(k) in answer:
                pass
            else:
                answer.append(int(k))

    return answer

print(solution(s))