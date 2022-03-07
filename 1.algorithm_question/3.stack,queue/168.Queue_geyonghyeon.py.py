import sys

input = sys.stdin.readline


def solution():
    answer = []
    t = int(input())
    for _ in range(t):
        n = int(input())
        card_list = input().split()
        temp_str = card_list[0]
        for i in card_list[1:]:
            if ord(i) <= ord(temp_str[0]):
                temp_str = f'{i}{temp_str}'
            else:
                temp_str = f'{temp_str}{i}'
        answer.append(temp_str)
    print('\n'.join(answer))


solution()
