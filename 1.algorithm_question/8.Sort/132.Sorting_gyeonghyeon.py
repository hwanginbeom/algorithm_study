import sys

input = sys.stdin.readline

n = int(input())
_dict = {}
for _ in range(n):
    _text = input().strip()
    _dict[_text] = len(_text)

_list = sorted(_dict.items(), key=lambda x:(x[1], x[0]))
for i in _list:
    print(i[0])