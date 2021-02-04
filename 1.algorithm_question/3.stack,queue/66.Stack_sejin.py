# 퐁당퐁당 안된다 선입후출 !

import sys
input = sys.stdin.readline

n = int(input())

count = 0
for _ in range(n) :
    word = list(map(str, input()))
    word.pop() # 맨뒤에 '/n'를 제거 위함

    stack = []
    for i in range(len(word)) :
        if len(stack) == 0 :
            stack.append(word[i])
        else :
            if word[i] == stack[-1] :
                stack.pop()
            else :
                stack.append(word[i])

    if len(stack) == 0 :
        count += 1

print(count)
