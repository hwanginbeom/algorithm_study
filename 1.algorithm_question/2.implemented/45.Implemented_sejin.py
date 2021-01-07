t = int(input())
for _ in range(t) :
    # 호텔 층 수, 각 층 방 수, 몇 번쨰 손님
    h, w, n = map(int, input().split())

    count = 0
    x,y = 0,0

    for i in range(w) :
        for j in range(h) :
            count += 1
            if count == n :
                x,y = i,j
                break

    # zfill(width) : 정해진 길이에서 앞에 0을 붙여주고 싶을 때
    # rjust(width, [fillchar])
    print(str(y+1) + str(x+1).zfill(2))