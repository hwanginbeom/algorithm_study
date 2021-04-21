n = int(input())
h = sorted(list(map(int, input().split())))
ans = 10 ** 10

for i in range(n):
    for j in range(i + 1, n):

        s1 = h[i] + h[j]  # 눈사람1 높이
        a = i
        b = n - 1
        while True:
            # li[i], li[j]는 이미 사용한 눈덩이이므로 넘겨줘야 한다.
            while a == i or a == j:
                a += 1
            while b == i or b == j:
                b -= 1

            if a >= b:
                break

            s2 = h[a] + h[b]  # 눈사람2 높이
            if s1 < s2:
                ans = min(ans, s2 - s1)
                b -= 1
            elif s1 >= s2:
                ans = min(ans, s1 - s2)
                a += 1
print(ans)