# 1. isdigit(), isalpha(),,, 각각 특성에 맞게 분리
# 2. 정수가 0부터 10 사이까지 가능해서 0과 10이 문제

def solution(dartResult):
    dart = dartResult
    list = []

    for i in range(len(dart)):

        if dart[i] == '1' and dart[i + 1] == '0':
            list.append('10')
        elif dart[i] == '0' and dart[i - 1] == '1':
            pass
        else:
            list.append(dart[i])
    print(list)

    answer = []
    for i in range(1, len(list)):

        if list[i] == 'S':  # 1제곱
            answer.append(int(list[i - 1]))
        elif list[i] == 'D':  # 2제곱
            answer.append(int(list[i - 1]) ** 2)
        elif list[i] == 'T':  # 3제곱
            answer.append(int(list[i - 1]) ** 3)
        print(answer)

        if list[i] == '*':  # 각 2배
            if len(answer) >= 2:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
            else:
                answer[-1] = answer[-1] * 2
        elif list[i] == '#':  # 마이너스
            answer[-1] = answer[-1] * (-1)

    result = sum(answer)
    return result