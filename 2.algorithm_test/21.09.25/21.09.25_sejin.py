def solution(s):
    s = s[2:-2].split('},{')
    s_lst = []
    for i in s:
        s_lst.append(list(map(int, i.split(','))))
    s_lst = sorted(s_lst, key=lambda x: len(x))

    answer = s_lst[0]
    for j in range(1, len(s_lst)):
        answer.extend(set(s_lst[j]) - set(s_lst[j - 1]))

    return answer
