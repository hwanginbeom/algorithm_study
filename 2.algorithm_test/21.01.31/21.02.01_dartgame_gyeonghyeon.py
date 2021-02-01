import re

def solution(dartResult):
    dartResult = [i for i in re.split(r'([0-9]+)|(#)|(\*)', dartResult) if i not in ['',None]]
    score = []
    score2 = []
    print(dartResult)
    for i,val in enumerate(dartResult):
        if val in ['D', 'S', 'T']:
            if val == 'D':
                score.append(int(dartResult[i - 1]) ** 2)
            elif val == 'S':
                score.append(int(dartResult[i - 1]) ** 1)
            else:
                score.append(int(dartResult[i - 1]) ** 3)
        elif val in ['#', '*']:
            score.append(dartResult[i])
        else:
            continue
    for idx, value in enumerate(score):
        print(score2)
        if value == '*' and idx > 1:
            ssuumm2 = (score2[-2] * 2) + (score2[-1] * 2)
            score2[-2] = score2[-2] * 2
            score2[-1] = score2[-1] * 2
        elif value == '*' and idx == 1:
            score2[-1] = score[idx - 1] * 2
        elif value == '#':
            score2[-1] = (score[idx - 1] * -1)
        else:
            score2.append(score[idx])
    answer = sum(score2)
    return answer


a = '1S2D3T*'
solution(a)