n = int(input())
data = list(map(int, input().split()))
data.sort()
x = int(input())

count = 0
end = len(data)-1

for start in range(len(data)) :
    two_sum = data[start]

    while start < end :
        two_sum += data[end]

        if two_sum == x :
            count += 1
            break
        elif two_sum > x :
            two_sum -= data[end]
            end -= 1
        else :
            break
print(count)


# 시간초과
#
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
# x = int(input())
#
# count = 0
#
# for start in range(len(data)):
#     for end in range(start, len(data)):
#         if data[start] + data[end] == x:
#             count += 1
#             pass
# print(count)


# 시간초과
#
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
# x = int(input())
#
# count = 0
#
# for start in range(len(data)//2+1) :
#     two_sum = data[start]
#     for end in range(len(data)-1, len(data)//2, -1) :
#         two_sum += data[end]
#         if two_sum == x:
#             count += 1
#             pass
#         else :
#             two_sum -= data[end]
# print(count)