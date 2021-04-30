num = 0

while 1:
    num += 1
    stack = []
    count = 0
    data = input()

    if '-' in data:
        break

    # 선입후출 stack
    for i in range(len(data)):
        if len(stack)==0 and data[i]=='}':
            count += 1
            stack.append('{')
        elif len(stack)!=0 and (data[i]=='}'):
            stack.pop()
        else:
            stack.append(data[i])

    count += len(stack)//2
    print(str(num) + '. ' + str(count))



