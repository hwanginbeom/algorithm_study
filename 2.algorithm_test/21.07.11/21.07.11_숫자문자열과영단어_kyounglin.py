# 2021-07-12

# 숫자 문자열과 영단어

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/81301?language=python3


# s='one4seveneight'
s = '23four5six7'


def solution(s):
    dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    str_val = ''
    answer = ''

    for i in list(s):
        if i.isalpha():  # 리스트 값이 문자
            str_val += i  # 문자열 합치기

            if str_val in dict:
                answer += str(dict[str_val])
                str_val = ''  # 딕셔너리안에 숫자 단어 있으면 초기화
        else:
            answer += str(i)

    return int(answer)

print(solution(s))