def solution(n, numlist):
    num, answer = [], [1]

    for i in range(2, n + 1):
        num.append(i)

    move = numlist.pop(0)
    loc = 0

    for _ in range(n - 1):
        if move < 0:
            loc = (loc + move) % len(numlist)
        else:
            loc = (loc + (move - 1)) % len(numlist)
        answer.append(num.pop(loc))
        move = numlist.pop(loc)

    print(' '.join(map(str, answer)))
    return


n = int(input())
bool_list = list(map(int, input().split()))
solution(n,bool_list)
