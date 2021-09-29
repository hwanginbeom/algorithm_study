def solution(scores):
    result = ''

    # 각 학생에게 평가된 점수를 리스트 s로 변환
    for i in range(len(scores)):
        s = []
        for j in range(len(scores)):
            s.append(scores[j][i])
        # min, max에 해당하면서 유일값이면 해당 점수 제거
        if s[i] == min(s) and s.count(s[i]) == 1:
            del s[i]
        elif s[i] == max(s) and s.count(s[i]) == 1:
            del s[i]

        mean = sum(s) / len(s)

        # 학점 변환
        if mean >= 90:
            result += 'A'
        elif mean >= 80:
            result += 'B'
        elif mean >= 70:
            result += 'C'
        elif mean >= 50:
            result += 'D'
        else:
            result += 'F'
    return result