# 2021-07-13

# 출처 : https://www.acmicpc.net/problem/7600

# 문자가 몇갤까

import re

while True:
    sentence = input()
    if sentence == '#':
        break
    print(len(set(re.findall('[a-zA-Z]', sentence.upper()))))