import re


def solution(str1, str2):
    str1_dict, str2_dict= {}, {}
    for name in zip([str1, str2], [str1_dict, str2_dict]):
        for i in range(len(name[0]) - 1):
            upper_str = name[0][i:i+2].upper()
            if len(re.findall(r'[A-Z]', upper_str)) == 2:
                name[1][upper_str] = name[1].get(upper_str, 0) + 1
    uni = 0
    for i in str1_dict:
        if i in str2_dict:
            uni += min(str1_dict[i], str2_dict[i])

    answer = sum(str1_dict.values()) + sum(str2_dict.values()) - uni
    if answer == 0:
        return 65536
    return int(65536 * uni / answer)






str1 = "FRANCE"
str2 = "french"
solution(str1, str2)