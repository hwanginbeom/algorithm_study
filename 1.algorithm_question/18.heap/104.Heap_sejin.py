num_list = []

for i in range(int(input())):
    num = int(input())
    num_list.append(num)

num_sort = sorted(num_list)

for j in num_sort:
    print(j)