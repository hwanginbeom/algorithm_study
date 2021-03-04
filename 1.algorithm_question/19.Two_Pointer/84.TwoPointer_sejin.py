n = int(input())
data = list(map(int, input().split()))
data.sort()
x = int(input())

count = 0
start = 0
end = len(data)-1

while start < end :
    two_sum = data[start] + data[end]
    if two_sum == x :
        count += 1
    elif two_sum < x :
        start += 1
        continue
    end -= 1
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