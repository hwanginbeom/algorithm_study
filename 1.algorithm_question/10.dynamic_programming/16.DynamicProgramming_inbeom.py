# 2839
value = int(input())

count = value // 5
box = 0

while(1):
    if count == -1:
        box = -1
        break
    if count == 0:
        if value % 3 == 0:
            box = value//3
            break
        else:
            box = -1
            break
    elif (value - (count*5)) % 3 == 0:
        count2 = (value - (count * 5)) // 3
        box = count + count2
        break
    else:
        count = count-1

print(box)



# #1463
#
# value = int(input())
#
# count = 0
#
# while(1):
#     if value <= 1:
#         break
#     if value % 3 == 1:
#         value = value - 1
#         count += 1
#     elif value % 3 == 0:
#         value = value / 3
#         count += 1
#     elif value % 2 == 0:
#         value = value / 2
#         count += 1
#     else:
#         value = value - 1
#         count += 1
#
# print(count)

n = int(input())

dp = [0 for _ in range(n + 1)]

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1

print(dp[n])
