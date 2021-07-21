
import sys
n = int(sys.stdin.readline())

stack=[]
for i in range(n):
    command = sys.stdin.readline().split() #split해서 입력 받기!

    #command가 push라면
    if command[0]=='push':
        stack.append(command[1])

    #command가 pop라면
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())

    #command가 size라면
    elif command[0] == 'size':
        print(len(stack))

    #command가 empty라면
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)

    #command가 top라면면
    elif command[0] == 'top':
        if ln(stack)==0:
            print(-1)
        else:
            print(stack[-1])
