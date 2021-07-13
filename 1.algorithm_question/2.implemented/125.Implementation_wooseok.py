# 문자가 몇갤까
# https://www.acmicpc.net/problem/7600


def solution() :
    answer = []

    while True :
        sentence = input()

        if sentence == '#' :
            break

        alpha_dict = {}
        sentence = sentence.lower()

        for s in sentence :
            if s.isalpha() :
                if s not in alpha_dict.keys() :
                    alpha_dict[s] = True

        answer.append(len(alpha_dict))

    for i in answer :
        print(i)


solution()
