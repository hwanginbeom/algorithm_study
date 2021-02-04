n = int(input())

n_list = []
for i in range(n):
    n_list.append(list(input()))

count = 0
for i in n_list:
    stack=[]
    for j in range(len(i)):
        if len(stack) < 1:
            stack.append(i[j])
        else :
            if stack[-1] == i[j]:
                stack.pop()
    else:
        if len(stack) == 0:
            count +=1
print(count)