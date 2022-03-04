import sys

input = sys.stdin.readline


def solution():
    text = input().strip()
    bomb = input().strip()
    bomb_length = len(bomb)
    bomb_last = bomb[-1]
    answer = []
    for txt in text:
        answer.append(txt)
        if txt == bomb_last and ''.join(answer[-bomb_length:]) == bomb:
            for _ in range(bomb_length):
                answer.pop()
    if answer:
        print(''.join(answer))
    else:
        print('FRULA')

solution()