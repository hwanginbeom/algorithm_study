n = int(input())

n_list = []

for i in range(n) :
    num = int(input())
    n_list.append(num)

n_list.sort()

# 평균
n_avg = int(round(sum(n_list) / len(n_list), 0))

# 중앙값
n_center = n_list[len(n_list) // 2]

n_mode = {}

for i in n_list :
    # print(i)
    if i not in n_mode.keys() :
        n_mode[i] = 0
        n_mode[i] += 1
        continue

    n_mode[i] += 1

n_mode = sorted(n_mode.items(), reverse = True, key = lambda item : item[1])

# 최빈값
if len(n_list) == 1 :
    n_mode = n_mode[0][0]
else :
    if n_mode[0][1] == n_mode[1][1] :
        n_mode = n_mode[1][0]
    else :
        n_mode = n_mode[0][0]

n_max = max(n_list)
n_min = min(n_list)

# 범위
n_range = n_max - n_min

print(n_avg)
print(n_center)
print(n_mode)
print(n_range)
