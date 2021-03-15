# 2021-03-15

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/64065

# 튜플

#s="{{2},{2,1},{2,1,3},{2,1,3,4}}"
#s="{{1,2,3},{2,1},{1,2,4,3},{2}}"
s="{{20,111},{111}}"

import re

def solution(s):
    # }, 로 분리하여 리스트 만든 후 리스트에서 숫자 값들만 array에 담음
    array=[re.findall('\d+',s.split('},')[i]) for i in range(len(s.split('},')))]
    array=sorted(array,key=len) # list 길이 순으로 정렬
    answer=[]
    for i in array:
        for j in i:
            if j in answer: # 중복되는 값이 존재하면 pass
                pass
            else:
                answer.append(j)

    return list(map(int,answer)) # 리스트의 값을 숫자로 변경

print(solution(s))

# 차집합 이용하면 시간 단축이 가능함!!
