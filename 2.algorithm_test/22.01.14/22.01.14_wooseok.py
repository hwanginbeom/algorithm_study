# 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301
import re


def solution(s):
    answer = 0
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(10):
        s = re.sub(num[i], str(i), s)

    answer = int(s)
    return answer


s = "one4seveneight"
print(solution(s))
