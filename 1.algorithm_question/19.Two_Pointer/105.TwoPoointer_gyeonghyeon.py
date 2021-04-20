import sys
input = sys.stdin.readline

n = int(input())
snow = sorted(list(map(int, input().split())))


def snowman():
    answer = int(1e9)
    for i in range(n - 1):
        for j in range(i + 1, n):
            snow_man_1 = snow[i] + snow[j]
            start = 0
            end = n - 1
            while start < end:
                if start == i or start == j:
                    start += 1
                    continue
                if end == i or end == j:
                    end -= 1
                    continue

                snow_man_2 = snow[start] + snow[end]
                answer = min(answer, abs(snow_man_1 - snow_man_2))
                if snow_man_2 < snow_man_1:
                    start += 1
                elif snow_man_2 > snow_man_1:
                    end -= 1
                else:
                    start += 1
                    end -= 1
    print(answer)

snowman()