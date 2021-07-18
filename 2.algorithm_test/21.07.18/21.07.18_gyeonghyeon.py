import re

def solution(str1, str2):
    str1_2, str2_2 = {},{}
    for name in zip([str1, str2],[str1_2, str2_2]):
        for i in range(len(name[0]) - 1):
            if len(re.findall(r'[A-Z]', name[0][i:i + 2].upper())) == 2:
                name[1][name[0][i:i + 2].upper()] = name[1].get(name[0][i:i + 2].upper(),0) +1
    uni = 0
    for idx in str1_2:
        if idx in str2_2:
            uni += min(str1_2[idx],str2_2[idx])

    answer = sum(str1_2.values()) + sum(str2_2.values()) - uni
    if answer == 0:
        return 65536
    return int(65536 * uni / answer)