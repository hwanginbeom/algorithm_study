import sys, math

input = sys.stdin.readline


def solution():
    range_number = 1000
    prime_array = [True for _ in range(range_number + 1)]
    for i in range(2, int(math.sqrt(range_number)) + 1):
        if prime_array[i]:
            j = 2
            while i * j <= range_number:
                prime_array[i * j] = False
                j += 1
    n = int(input())
    answer = []
    for i in list(map(int, input().split())):
        if i == 1:
            continue
        else:
            if prime_array[i]:
                answer.append(i)
    print(len(answer))

solution()