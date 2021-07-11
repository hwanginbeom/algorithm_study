# 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301


def solution(s):
    answer = ''

    _dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    alpha = ''
    for i in s:
        if i.isalpha():
            alpha += i

            if alpha in _dict.keys():
                answer += str(_dict[alpha])
                alpha = ''
        else:
            answer += i

    return int(answer)


s = 'one4seveneight'
print(solution(s))

