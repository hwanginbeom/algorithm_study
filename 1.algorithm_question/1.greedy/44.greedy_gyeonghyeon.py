n = int(input())
num_list = sorted(list(map(int, input().split())))
result = 0
for i in range(len(num_list)+1):
    result += sum(num_list[0:i])
print(result)
