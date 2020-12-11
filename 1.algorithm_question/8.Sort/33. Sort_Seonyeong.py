## 1431번: 시리얼 번호

#### 나의 첫 풀이 : 한번에 조건이 적용되지 않아서 조건은 제대로 적용되나 최종값의 순서가 뒤죽박죽이 된다.
# import time
#
# n = int(input())
# guitars = []
#
# for _ in range(n):
#     guitar = input()
#     guitars.append(guitar)
#
# start_time = time.time()
#
# for i in range(len(guitars)):
#     min_index = i
#     for j in range(i+1, len(guitars)):
#         if len(guitars[min_index]) > len(guitars[j]):
#             min_index = j
#             guitars[i], guitars[min_index] = guitars[min_index], guitars[i]
#             print('guitars[i], guitars[min_index] - 1', guitars[i], guitars[min_index])
#         elif len(guitars[min_index]) == len(guitars[j]):
#             a = [int(i) for i in guitars[min_index] if i.isnumeric()]
#             b = [int(i) for i in guitars[j] if i.isnumeric()]
#             if sum(a) > sum(b):
#                 min_index = j
#                 guitars[i], guitars[min_index] = guitars[min_index], guitars[i]
#                 print('guitars[i], guitars[min_index] - 2', guitars[i], guitars[min_index])
#             if sum(a) == sum(b):
#                 if guitars[min_index] > guitars[j]:
#                     print('>>>>>',type(guitars[min_index]))
#                     min_index = j
#                     guitars[i], guitars[min_index] = guitars[min_index], guitars[i]
#                     print('guitars[i], guitars[min_index] - 3', guitars[i], guitars[min_index])
#
# print(guitars)
# end_time = time.time()
#
# print('time ', end_time - start_time)


def serial_sum(x):
    sum = 0

    for i in x:
        if i.isnumeric():
            sum += int(i)

    return sum

n = int(input())
guitars = []

for _ in range(n):
    guitars.append(input())

guitars = sorted(guitars, key=lambda x: (len(x), serial_sum(x), x))

for i in guitars:
    print(i)

