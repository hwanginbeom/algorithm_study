number = int(input())
number_list = []
for i in range(0,number):
    number_list.append(int(input()))
number_list.sort()
for i in number_list:
    print(i)