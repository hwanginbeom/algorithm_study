# 2021-03-06

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/17677

# 뉴스 클러스터링
from collections import Counter
import re

str1='aa1+aa2'
str2='AAAA12'


def solution(str1,str2):
    str1_list=[]
    str2_list=[]

    for i in range(len(str1)-1):
        check=str1[i:i+2]
        check=''.join(re.findall("[a-zA-Z]+", check))
        if len(check)==2:
            str1_list.append(check.upper())

    for i in range(len(str2)-1):
        check=str2[i:i+2]
        check=''.join(re.findall("[a-zA-Z]+", check))
        if len(check)==2:
            str2_list.append(check.upper())

    if len(str1_list)==0 and len(str2_list)==0:
        answer=65536
    else:
        inter_cnt=Counter(str1_list)&Counter(str2_list)
        intersection=len(list(inter_cnt.elements()))

        union_cnt=Counter(str1_list)|Counter(str2_list)
        union=len(list(union_cnt.elements()))

        answer=(intersection/union)*65536

    return int(answer)

print(solution(str1,str2))
