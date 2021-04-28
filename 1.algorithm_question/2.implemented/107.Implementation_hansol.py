# 구현
# 파일 정리
# https://www.acmicpc.net/problem/20291

# 시간 초과
# N = int(input())
# answer = []
# for i in range(N):
#     filename = input()
#     name, extension = filename.split('.')
#     answer.append(extension)
#
# ans_set = sorted(set(answer))
# for i in ans_set:
#     print(i, answer.count(i))

import sys

input = sys.stdin.readline

# Dictionary 활용
n, file = int(input()), {}
for i in range(n):
    filename = input().split()[0].split('.')[1]
    file[filename] = file.get(filename, 0) + 1

for value in sorted(file.items()):
    print(value[0], value[1])