
def solution(s):
    answer = []
    s = s.replace('{', '')
    s = s.split('}')
    for i in range(len(s)-1, -1, -1):
        if s[i] == '':
            s.pop(i)
        else:
            s[i] = s[i].split(',')
            if i:
                s[i].pop(0)
            s[i] = list(map(int, s[i]))
    s = sorted(s, key=len)
    #여기까지가 정렬
    dic = {}
    for i in s:
        for j in i:
            if dic.get(j, -1) == -1:
                answer.append(j)
                dic[j] = 1
    return answer