def solution(weights, head2head):
    data = []

    for i in range(len(head2head)):
        head = list(head2head[i])

        # 승률
        if len(head2head) - head.count('N') == 0:
            a = 0
        else:
            a = head.count('W') / (len(head2head) - head.count('N')) * 100

        # 자기보다 무거운 복서를 이긴 횟수
        win_index = [i for i, x in enumerate(head) if x == 'W']
        b = 0
        for j in win_index:
            if weights[i] < weights[j]:
                b += 1

        # 추가로, 몸무게와 순서
        data.append([a, b, weights[i], i])

    data = sorted(data, key=lambda x: (-x[0], -x[1], -x[2], x[3]))
    answer = [k[3] + 1 for k in data]
    return answer