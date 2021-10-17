def solution(weights, head2head):
    answer = {}
    for idx, values in enumerate(zip(weights, head2head)):
        win_cnt = values[1].count('W')
        lose_cnt = values[1].count('L')
        try:
            per = win_cnt / (lose_cnt + win_cnt) * 100
        except:
            per = 0
        weight_cnt = 0
        for idx2, text in enumerate(values[1]):
            if text == 'W':
                if values[0] < weights[idx2]:
                    weight_cnt += 1
        answer[idx + 1] = [per, weight_cnt, values[0], idx + 1]
    answer = sorted(answer.items(), key=(lambda x: (-x[1][0], -x[1][1], -x[1][2], x[1][3])))
    answer = [i[0] for i in answer]
    return answer


weights = [50, 82, 75, 120]
head2head = ["NLWL", "WNLL", "LWNW", "WWLN"]
solution(weights, head2head)
