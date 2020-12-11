n = int(input())
num_list = [[] for _ in range(n)]
number_list = [str(i) for i in range(1,10)]
num = 0

for i in range(n):
    zip = input().strip()
    for j in zip:
        num_list[i].extend(j)
        if j in number_list:
            num += int(j)
    num_list[i].extend([num])
    num = 0

num_list = sorted(num_list, key=lambda x:(len(x), x[-1], x[::1]))
for i in num_list:
    print(''.join(i[:-1]))
