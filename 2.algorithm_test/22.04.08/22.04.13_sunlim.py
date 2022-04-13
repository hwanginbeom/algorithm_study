#뉴스클러스터링

import re
from collections import deque

def multi_set(text):
    text = deque(text)
    Q = deque(text.popleft())
    res = list()

    while text:
        Q.append(text.popleft())
        if len(re.findall('[a-z]', ''.join(Q))) == 2:
            res.append(''.join(Q))
        Q.popleft()
    return res

def solution(str1, str2):
    union, inter = 0, 0
    str1 = sorted(multi_set(str1.lower()))
    str2 = sorted(multi_set(str2.lower()))
    p1, p2 = len(str1) - 1, len(str2) - 1

    while str1 and str2:
        if str1[p1] == str2[p2]:
            str1.pop()
            str2.pop()
            union, inter = union + 1, inter + 1
            p1, p2 = p1 - 1, p2 - 1
        elif str1[p1] > str2[p2]:
            str1.pop()
            union += 1
            p1 -= 1
        else:
            str2.pop()
            union += 1
            p2 -= 1

    union = union + len(str1) + len(str2)
    if union == 0:
        return 65536
    return int(65536 * inter / union)