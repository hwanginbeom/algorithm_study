from collections import deque

n = int(input())

for i in range(n):
    function = input()
    number = int(input())
    number_list = input()
    number_list = number_list[1:-1]
    number_list = number_list .split(',')
    if number_list[0] == '':
        number_list = []
    number_lists = []
    if len(number_list) > 0:
        for i in range(0,len(number_list)):
            number_lists.append(int(number_list[i]))
    number_lists = deque(number_lists)
    count = 0
    for i in range(len(function)):
        if function[i] == 'R':
            count = (count+1) % 2
        elif function[i] == 'D':
            if len(number_lists) > 0 and count == 1:
                number_lists.pop()
            elif len(number_lists) > 0 and count == 0:
                number_lists.popleft()
            else:
                number_lists = 'error'
                break
    if number_lists == 'error':
        print(number_lists)
    elif count == 1:
        number_lists.reverse()
        print(str(list(number_lists)).replace(' ', ''))
    else:
        print(str(list(number_lists)).replace(' ', ''))