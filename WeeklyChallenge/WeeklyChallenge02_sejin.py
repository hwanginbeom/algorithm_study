import numpy as np

def grade(x):
    if x >= 90:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 50:
        return 'D'
    else:
        return 'F'
# [ avg >= 90 and "A" or avg >= 80 and "B" or avg >= 70 and "C" or avg >= 50 and "D" or "F" for avg in avgs ]

def solution(scores):
    scores = list(map(list, zip(*scores)))

    answer = []
    for i in range(len(scores)):
        myscore = scores[i][i]
        if (myscore != max(scores[i])) and (myscore != min(scores[i])):
            answer.append(np.mean(scores[i]))
        elif scores[i].count(myscore) != 1:
            answer.append(np.mean(scores[i]))
        else:
            scores[i].remove(myscore)
            answer.append(np.mean(scores[i]))

    answer = ''.join(list(map(grade, answer)))
    return answer
