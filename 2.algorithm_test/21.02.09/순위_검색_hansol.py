# 순위 검색
# https://programmers.co.kr/learn/courses/30/lessons/72412#

import bisect

def solution(info, query):
    answer = []

    language = ['cpp', 'java', 'python', '-']
    position = ['backend', 'frontend', '-']
    career = ['junior', 'senior', '-']
    food = ['chicken', 'pizza', '-']

    tables = {}
    for lang in language:
        for posi in position:
            for ca in career:
                for fo in food:
                    string = lang + posi + ca + fo
                    tables[string] = []

    for candidate in info:
        string = candidate.split(' ')
        language = [string[0], '-']
        position = [string[1], '-']
        career = [string[2], '-']
        food = [string[3], '-']

        for lang in language:
            for posi in position:
                for ca in career:
                    for fo in food:
                        key = lang + posi + ca + fo
                        tables[key].append(int(string[4]))

    for key, value in tables.items():
        tables[key] = sorted(value)

    for candidate in query:
        member = 0
        candi, score = candidate.replace(' and ', '').split(' ')
        score = int(score)
        size = len(tables[candi])
        num = size - bisect.bisect_left(tables[candi], score, lo=0, hi=size)

        answer.append(num)

    return answer