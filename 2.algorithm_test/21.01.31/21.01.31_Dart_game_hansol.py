# 다트 게임
# https://programmers.co.kr/learn/courses/30/lessons/17682

dartresult = input()

def solution(dartresult):
    score = []
    number = ''
    # 입력값의 문자를 하나씩 확인
    for i in dartresult:
        # 숫자이면 number 에 추가
        if i.isdigit():
            number += i
        # S, D, T 일 때 계산을 입력
        elif i == 'S':
            score.append(int(number))
            number=''
        elif i == 'D':
            score.append(int(number) ** 2)
            number=''
        elif i == 'T':
            score.append(int(number) ** 3)
            number = ''
        # * 일 때 두 가지 경우로 나누어 계산
        elif i == '*':
            if len(score) > 1:
                score[-2] *= 2
            score[-1] *= 2
            number = ''
        # # 일 때의 계산
        elif i == '#':
            score[-1] *= (-1)
    return sum(score)

print(solution(dartresult))