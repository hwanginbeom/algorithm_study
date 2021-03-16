T = int(input())
for _ in range(T) :
    a, b = map(int, input().split())

    a = int(str(a)[-1]) # 맨끝자리만 중요
    if a == 0:
        print(10)
        continue
    elif a == 1 | a == 5 | a == 6:
        print(a)
        continue

    lst = []
    x = 1
    for _ in range(b):
        x *= a
        x %= 10

        if x in lst:
            break
        else:
            lst.append(x)

    answer = lst[b % len(lst) - 1]
    print(answer)