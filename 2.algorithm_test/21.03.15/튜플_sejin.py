s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
s = s[2:-2].split('},{')
s = sorted(s, key = lambda x : len(x))
# print(s)

answer = []
for i in s:
    ss = i.split(',')
    for j in ss:
        if int(j) not in answer:
            answer.append(int(j))
print(answer)

# 요거 때매 오래걸렸다... 후 빡쳐
# 백준의 폐해....
# answer = '[' + ','.join(answer) + ']'

# 차집합으로 풀면 시간초를 줄일 수 있따
