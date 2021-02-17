n = int(input())
score = []
for _ in range(n):
    score.append(int(input()))

dp = []

# 이녀석 때문에 런타임 에러.... 이걸 뭔가 코드를 짧게 줄일 방법 없나
if n == 1 :
    print(score[0])
elif n == 2 :
    print(max(score[0]+score[1], score[1]))
elif n == 3 :
    print(max(score[0]+score[2], score[1]+score[2]))

else :
    dp.append(score[0])
    dp.append(max(score[0]+score[1], score[1]))
    dp.append(max(score[0]+score[2], score[1]+score[2]))

    for i in range(3, n):
        dp.append(max(dp[i-2]+score[i], dp[i-3]+score[i-1]+score[i]))
    print(dp[n-1])
