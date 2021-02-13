# 듣보잡
def solution() :
    n, m = map(int, input().split())

    no_listen = set()
    no_see = set()

    for _ in range(n) :
        no_listen.add(input())

    for _ in range(m) :
        no_see.add(input())

    # 교집합 구하기
    answer = no_listen.intersection(no_see)

    answer = list(answer)
    answer.sort()

    print(len(answer))
    for i in answer :
        print(i)


solution()
