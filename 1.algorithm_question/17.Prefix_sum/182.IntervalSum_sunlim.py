# -*- coding: utf-8 -*-


# 백준 2851 슈퍼마리오



m = []
score = 0
for i in range(10):
    m.append(int(input()))
for j in m:
    score += j
    if score >= 100:   #100이 넘어갈때 조건문걸기
        if score - 100 > 100 - (score - j):
            score -= j
        break
print(score)