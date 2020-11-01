#40분
def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []

    if len(one) < len(answers):
        one = one * ((len(answers) // len(one)) + 1)
    one = one[:len(answers)]
    if len(two) < len(answers):
        two = two * ((len(answers) // len(two)) + 1)
    two = two[:len(answers)]
    if len(thr) < len(answers):
        thr = thr * ((len(answers) // len(thr)) + 1)
    thr = thr[:len(answers)]

    one_count = 0
    two_count = 0
    thr_count = 0

    for i in range(0, len(one)):
        if one[i] == answers[i]:
            one_count+=1
    answer.append(one_count)

    for i in range(0, len(two)):
        if two[i] == answers[i]:
            two_count += 1
    answer.append(two_count)

    for i in range(0, len(thr)):
        if thr[i] == answers[i]:
            thr_count += 1
    answer.append(thr_count)

    m = max(answer)
    result = [i+1 for i, j in enumerate(answer) if j == m]
    print(result)
    return result

answer= [1,3,2,4,2]
solution(answer)
