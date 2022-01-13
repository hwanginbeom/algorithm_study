import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    number_card = set(map(int, input().split()))
    print(number_card)
    m = int(input())
    compare_card = set(map(int, input().split()))
    answer = []
    for i in compare_card:
        if i in number_card:
            answer.append(1)
        else:
            answer.append(0)
    print(' '.join(list(map(str,answer))))

solution()