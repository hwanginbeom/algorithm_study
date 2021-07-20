import re
from collections import Counter

def solution(str1, str2):
    str1_list = []
    str2_list = []

    for i in range(len(str1) - 1):
        check1 = str1[i:i + 2]
        check1 = re.findall('[a-zA-Z]+', check1)
        if len(check1) != 0 and len(check1[0]) == 2:
            str1_list.append(check1[0].upper())

    for j in range(len(str2) - 1):
        check2 = str2[j:j + 2]
        check2 = re.findall('[a-zA-Z]+', check2)
        if len(check2) != 0 and len(check2[0]) == 2:
            str2_list.append(check2[0].upper())

    interection = len(list((Counter(str1_list) & Counter(str2_list)).elements()))
    union = len(list((Counter(str1_list) | Counter(str2_list)).elements()))

    if len(str1_list) == 0 and len(str2_list) == 0:
        answer = 65536
    else:
        answer = int((interection / union) * 65536)

    return answer