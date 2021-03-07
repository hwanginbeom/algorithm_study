# 자카드 유사도 = 두 집합의 교집합 크기 / 두 집합의 합집합 크기
# 1) 영문자만 가능, 기타공백 숫자 특수문자가 있는 쌍은 버린다
# 2) 영문자의 대문자와 소문자 차이는 무시한다
# 3) 다중집합으로 확장 가능 => 교집합:min() 합집합:max()
# 4) 두 집합 모두 공집합 일 경우 답은 1로 정의

# Counter에서 교집합, 합집합이 읽힌다 !!

import re #정규표현식을 위한 모듈
from collections import Counter # 등장횟수를 위한 모듈

str1 = 'E=M*C^2'
str2 = 'e=m*c^2'

str1 = re.sub('[^a-zA-Z]',' ',str1).upper()
d1 = []
for i in range(len(str1)-1):
    string = str1[i:i+2]
    if string.isalpha() and not string.isspace():
        d1.append(string)

str2 = re.sub('[^a-zA-Z]',' ',str2).upper()
d2 = []
for i in range(len(str2)-1):
    string = str2[i:i+2]
    if string.isalpha() and not string.isspace():
        d2.append(string)


if (len(d1) == 0) and (len(d2) == 0): # 모두 공집합인 경우
    answer = 1*65536
else :
    intersection = Counter(d1)&Counter(d2) # 교집합
    union = Counter(d1)|Counter(d2) # 합집합

    a = sum([v for k,v in intersection.items()])
    b = sum([v for k,v in union.items()])
    answer = a/b*65536
print(int(answer))


# 문제에서 주어진대로 min과 max를 구해서 푸는 형식
#
# import re
# import math
#
# str1 = 'handshake'
# str2 = 'shake hands'
#
# str1 = re.sub('[^a-zA-Z]',' ',str1).upper()
# d1 = []
# for i in range(len(str1)-1):
#     string = str1[i:i+2]
#     if string.isalpha() and not string.isspace():
#         d1.append(string)
#
# str2 = re.sub('[^a-zA-Z]',' ',str2).upper()
# d2 = []
# for i in range(len(str2)-1):
#     string = str2[i:i+2]
#     if string.isalpha() and not string.isspace():
#         d2.append(string)
#
# intersection = set(d1)&set(d2)
# union = set(d1)|set(d2)
#
# if len(union) == 0 :
#     answer = 1*65536
# else :
#     a = sum([min(d1.count(i), d2.count(i)) for i in intersection])
#     b = sum([max(d1.count(i), d2.count(i)) for i in union])
#     answer = a/b*65536
# print(int(answer))