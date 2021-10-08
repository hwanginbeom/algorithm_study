import itertools

def solution(word):
    dict = []
    for i in range(1, 6):
        dict.extend(list(map(''.join, itertools.product('AEIOU', repeat=i))))
    dict.sort()
    return dict.index(word)+1
