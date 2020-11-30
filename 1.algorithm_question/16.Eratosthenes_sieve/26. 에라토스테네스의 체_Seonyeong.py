## 2960번: 에라토스테네스의 체

import math

n, k = map(int, input().split())

array = [True for i in range(n+1)]

cnt = 0
for i in range(2, n+1):

    if array[i] is True:
        j = 1
        while i * j <= n:
            if array[i*j] is False:
                j += 1

            else:
                array[i*j] = False
                cnt += 1
                j += 1

                if cnt == k:
                    print(i*(j-1))
                    break


# import math
#
#
# def solution1() :
#     n, k = map(int, input().split())
#
#     array = [True for _ in range(n + 1)]
#     count = 0
#     result = 0
#     isFlag = False
#
#     for i in range(2, int(math.sqrt(n)) + 1) :
#         if array[i] is True :
#             j = 1
#
#             while i * j <= n :
#                 if array[i * j] is False :
#                     j += 1
#                     continue
#
#                 array[i * j] = False
#
#                 count += 1
#
#                 if count == k :
#                     isFlag = True
#                     result = i * j
#                     break
#
#                 j += 1
#
#             if isFlag :
#                 break
#
#     print(result)


