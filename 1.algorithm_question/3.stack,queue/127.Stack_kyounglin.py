# 2021-07-21
# 출처 : https://www.acmicpc.net/problem/10828

# 스택

n=int(input())

stack=[]
answer=[]

for _ in range(n):
    x=input().split()
    if x[0]=='push':
        stack.append(int(x[-1]))
    elif x[0]=='top':
        if len(stack)==0:
            answer.append(-1)
        else:
            answer.append(stack[-1])
    elif x[0]=='size':
        answer.append(len(stack))
    elif x[0]=='empty':
        if len(stack)==0:
            answer.append(1)
        else:
            answer.append(0)
    elif x[0]=='pop':
        if len(stack)==0:
            answer.append(-1)
        else:
            answer.append(stack.pop())

for i in answer:
    print(i)