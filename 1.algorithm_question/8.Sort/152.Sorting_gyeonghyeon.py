import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    answer = []
    for i in range(n):
        age, name = input().split()
        answer.append([i,int(age), name])
    answer.sort(key=lambda x:(x[1], x[0]))
    for j in answer:
        print(f'{j[1]} {j[2]}')
solution()