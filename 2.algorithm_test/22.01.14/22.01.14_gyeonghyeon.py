import sys

input = sys.stdin.readline

eng_list = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
            'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def solution(s):
    for idx, value in eng_list.items():
        s = s.replace(idx, str(value))
    return int(s)