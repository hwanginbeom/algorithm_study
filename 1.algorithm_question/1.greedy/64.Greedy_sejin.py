# plus 길이 2 이상 minus 길이 2 이상
# plus 길이 2 이상 : 1이 있는 경우, 나머지
    # 1 2 => 더하는게 낫네
# minus 길이 2 이상 : 0과 -1이 있는 경우, 나머지
    # -1 0 =>  곱하는게 낫네
    # -2 -1 => 곱하는게 낫네

import sys
input = sys.stdin.readline

n = int(input())
plus = []
minus = []
answer = 0

for _ in range(n) :
    m = int(input())
    if m > 0 :
        plus.append(m)
    elif m == 1 :
        answer += 1
    else :
        minus.append(m)
plus.sort(reverse=True)
minus.sort()

for i in range(0, len(plus)-1, 2) :
    answer += plus[i] * plus[i+1]
if len(plus) % 2 != 0 :
    answer += plus[-1]

for i in range(0, len(minus)-1, 2) :
    answer += minus[i] * minus[i + 1]
if len(minus) % 2 != 0 :
    answer += minus[-1]
print(answer)
