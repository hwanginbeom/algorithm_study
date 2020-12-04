## 15651번: N과 M(3)
from itertools import product
n, m = map(int, input().split())

a = product(range(1,n+1), repeat=m)

for i in a:
    print(*i)


## 14888번: 연산자 끼워넣기

from itertools import permutations

n = int(input())

A = list(map(int, input().split()))
plus, minus, multiple, division = map(int, input().split())

# 입력된 각각의 연산자를 담기
operation_list = []
operation_list += [1] * plus
operation_list += [2] * minus
operation_list += [3] * multiple
operation_list += [4] * division


operation_set = []
for numbers in list(permutations(operation_list)):
    operation_set.append(numbers)
print(operation_set)
operation_set = list(set(operation_set))

min_answer = 1000000001
max_answer = -1000000001

for case in operation_set:
    answer = A[0]

    for i in range(n-1):
        if case[i] == 1:
            answer += A[i+1]
        elif case[i] == 2:
            answer -= A[i+1]
        elif case[i] == 3:
            answer *= A[i+1]
        elif case[i] == 4:
            if answer < 0:
                answer = -(answer // A[i+1])
            else:
                answer //= A[i+1]
    if answer > max_answer:
        max_answer = answer
    if answer < min_answer:
        min_answer = answer

print(max_answer)
print(min_answer)