import math

def max_num(a,b,c):
    c_2 = c**2
    a_b = (a**2)+(b**2)
    if c_2 == a_b:
        return print('right')
    else:
        return print('wrong')

while True:
    num_list = sorted(list(map(int, input().split())))
    if num_list[0] != 0 and num_list[1] != 0 and num_list[2] != 0:
        max_num(num_list[0], num_list[1], num_list[2])
    elif num_list[0] == 0 and num_list[1] == 0 and num_list[2] == 0:
        break