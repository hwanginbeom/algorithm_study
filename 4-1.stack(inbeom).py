# 파이썬이 동적변수라지만 변수의 형태로 저장하기 위해서 input() 메소드 내에서 가공을 할텐데
#
# raw_input() 은 문자열을 반환하고 input() 은 raw_input() 을 evaluate한 결과를 반환합니다.
#
# sys.stdin.readline() 은 한 줄의 문자열를 반환하는데 이것을 int() 로 묶어서 정수로 변환하는게 더 빠른가봅니다.
import sys

input = sys.stdin.readline


stack_list = []

number = int(input())

for i in range(number):
    Command = input().split()
    if Command[0] == 'push' and len(Command) == 2 :
        stack_list.append(Command[1])
    elif Command[0] == 'pop':
        if len(stack_list) > 0:
            print(stack_list[-1])
            stack_list.pop()
        else:
            print('-1')
    elif Command[0] == 'size':
        print(len(stack_list))
    elif Command[0] == 'empty':
        if len(stack_list) > 0:
            print('0')
        else:
            print('1')
    elif Command[0] == 'top':
        if len(stack_list) > 0:
            print(stack_list[-1])
        else:
            print('-1')
    else:
        continue

