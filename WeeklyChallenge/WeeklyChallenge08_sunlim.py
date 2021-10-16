#WeeklyChallenge 8주차_ 최소직사각형
# 명함 가로,세로길이 조사함> 명함 가로,세로 길이를 나타내는 2차원배열이 매개변수이고, 모든 명함을 수납할수 있는 가장 작은 지갑 만드기

## 카드는 회전이 가능하기때문에 여러장의 카드의 최소 가로/세로를 구하려면
# 각 카드의 짧은 부분끼리 비교하고 긴부분끼리 비교하면 된다.

def solution(sizes):
    w,h=0,0

    for i in sizes:
        if w< max(i[0],i[1]): w=max(i[0],i[1])
        if h < min (i[0], i[1]): h = min(i[0], i[1])

    return  w*h

