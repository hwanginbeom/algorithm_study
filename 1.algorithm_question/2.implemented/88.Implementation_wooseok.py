# 분산처리
# https://www.acmicpc.net/problem/1009


def solution() :
    t = int(input())
    answer = []

    for _ in range(t) :
        a, b = map(int, input().split())

        _list = []
        result = a

        if result % 10 == 0 :
            _list.append(10)
        else :
            while True :
                if result == 10 :
                    _list.append(10)
                    break

                temp = result % 10

                if temp not in _list :
                    _list.append(temp)
                else :
                    break

                result *= a

        cycle = b % len(_list)

        if cycle == 0 :
            answer.append(_list[-1])
        else :
            answer.append(_list[cycle - 1])

    for i in answer :
        print(i)


solution()
