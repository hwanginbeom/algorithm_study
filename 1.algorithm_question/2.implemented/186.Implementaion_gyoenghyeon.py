import sys

input = sys.stdin.readline


def solution():
    alphabet_01 = ['c=', 'c-', 'lj', 'nj', 's=', 'z=']
    check_list = ['c', 'd', 'l', 'n', 's', 'z']
    text = list(input())
    start = 0
    answer = 0
    while start < (len(text) - 1):
        if text[start] in check_list:
            if text[start] != 'd':
                if ''.join(text[start: start + 2]) in alphabet_01:
                    start += 2
                else:
                    start += 1
            else:
                if ''.join(text[start:start + 2]) == 'd-':
                    start += 2
                elif ''.join(text[start:start + 3]) == 'dz=':
                    start += 3
                else:
                    start += 1
            answer += 1
        else:
            answer += 1
            start += 1
    return answer


print(solution())
