# 2022-01-19

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/81301

# 숫자 문자열과 영단어

import re

s = 'one4seveneight'

def solution(s):
    dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
            'nine': 9}

    answer = ''
    english = ''
    for i in s:
        if i.isdigit():
            answer += i
        else:
            english += i
            if english in list(dict.keys()):
                answer += str(dict[english])
                english = ''

    return int(answer)

print(solution(s))