import math

n = list(map(int,input()))

set_count = [0 for _ in range(10)]

for i in range(len(n)) :
    set_count[n[i]] += 1

set_count[6] = set_count[9] = math.ceil((set_count[6]+set_count[9])/2)
answer = max(set_count)

print(answer)