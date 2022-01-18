# 2022-01-18

# 출처 : https://www.acmicpc.net/problem/2839

# 설탕 배달

N = int(input())

cnt = 0

while True:
    if N%5==0: #5로 나누어 떨어질때 가장 봉지수가 적음
        cnt += N//5
        break
    else: # 5로 나누어 떨어지지 않을경우 무조건 3kg에 넣어야 하기 때문에 3kg 가져갈때마다 봉지수 증가
        N = N-3
        cnt+=1
        if N==1 or N==2: # 3과 5로 나누어 떨어지지 않을 경우
            cnt = -1
            break
print(cnt)