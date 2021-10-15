# 2021-10-15

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/86491

# 위클리 챌린지 - 8주차_최소직사각형

#sizes=[[60, 50], [30, 70], [60, 30], [80, 40]]
sizes=[[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]

def solution(sizes):
    long=[]
    short=[]

    for i in sizes:
        if i[0]<i[1]:
            long.append(i[1])
            short.append(i[0])
        else:
            long.append(i[0])
            short.append(i[1])

    return max(long)*max(short)

print(solution(sizes))