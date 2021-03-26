# 2021-03-25

# 출처 : https://www.acmicpc.net/problem/11726

# 2×n 타일링

# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
#
# 아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.

n=int(input())

array=[0]*(n+1)

for i in range(1,n+1):
    if i==1:
        array[i]=1
        continue # 아래 실행 x 바로 패스
    elif i==2:
        array[i]=2
        continue
    array[i]=array[i-1]+array[i-2]


print(array[n]%10007)