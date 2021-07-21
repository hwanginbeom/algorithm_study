import re
import math

def solution(str1, str2):
    str1 = re.sub('[^a-zA-Z]', ' ', str1).upper()
    d1 = []
    for i in range(len(str1) - 1):
        string = str1[i:i + 2]
        if string.isalpha() and not string.isspace():
            d1.append(string)

    str2 = re.sub('[^a-zA-Z]', ' ', str2).upper()
    d2 = []
    for i in range(len(str2) - 1):
        string = str2[i:i + 2]
        if string.isalpha() and not string.isspace():
            d2.append(string)

    intersection = set(d1) & set(d2)
    union = set(d1) | set(d2)

    if len(union) == 0:
        answer = 1 * 65536
    else:
        a = sum([min(d1.count(i), d2.count(i)) for i in intersection])
        b = sum([max(d1.count(i), d2.count(i)) for i in union])
        answer = a / b * 65536
    return int(answer)
