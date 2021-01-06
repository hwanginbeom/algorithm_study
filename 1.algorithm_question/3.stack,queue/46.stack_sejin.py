t = int(input())

for _ in range(t) :
    data = input()

    stack = []
    check = 0

    for i in data :
        if i == '(' :
            stack.append(i)
        elif i == ')' :
            if len(stack) == 0 :
                print("NO")
                check = 1
                break
            else :
                stack.pop(-1)

    if len(stack) != 0 and check == 0 :
        print("N0")
    elif len(stack) == 0 and check == 0 :
        print("YES")

# 스택 알고리즘이 아닌 코딩
#
# t = int(input())
# for _ in range(t) :
#     data = list(input())
#
#     count = 0
#
#     for i in data :
#         if i == '(' :
#             count += 1
#         elif i == ')' :
#             count -= 1
#         if count < 0 :
#             print("NO")
#             break
#
#     if count > 0 :
#         print("NO")
#     elif count == 0 :
#         print("YES")