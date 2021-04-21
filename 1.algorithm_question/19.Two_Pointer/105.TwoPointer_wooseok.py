# 같이 눈사람 만들래?
# https://www.acmicpc.net/problem/20366


def solution() :
    n = int(input())
    snowball = list(map(int, input().split()))

    snowball.sort()
    diff = 10 ** 9

    for i in range(n) :
        for j in range(i + 1, n) :
            elsa = snowball[i] + snowball[j]

            anna_start = i
            anna_end = n - 1

            while True :
                # 이미 골라진 눈덩이는 다시 선택되면 안된다.
                while anna_start == i or anna_start == j :
                    anna_start += 1
                while anna_end == i or anna_end == j :
                    anna_end -= 1

                if anna_start >= anna_end :
                    break

                anna = snowball[anna_start] + snowball[anna_end]

                if elsa < anna :
                    diff = min(diff, anna - elsa)
                    anna_end -= 1
                else :
                    diff = min(diff, elsa - anna)
                    anna_start += 1

    print(diff)


solution()
