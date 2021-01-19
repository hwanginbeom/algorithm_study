def solution(files):
    answer = []
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    tmp_result = []
    for f in range(len(files)):
        head, number, tail = '', '', ''
        idx, num_cnt = 0, 0
        for h in range(idx, len(files[f])):
            if files[f][h] in num:
                break
            head += files[f][h]
            idx += 1

        for n in range(idx, len(files[f])):
            if not files[f][n] in num:
                break
            if len(number) <= 5:
                if files[f][n] in num:
                    number += files[f][n]
                    idx += 1
            else:
                break
        # print(number)
        if idx < len(files[f]):
            for t in range(idx, len(files[f])):
                if files[f][t]:
                    tail += files[f][t]
                else:
                    break
        # print(tail)
        tmp_result.append((head.lower(), int(number), tail, f))
        tmp_result = sorted(tmp_result, key=lambda x: (x[0], x[1]))
    print(tmp_result)
    for i in tmp_result:
        answer.append(files[i[3]])
    return answer
