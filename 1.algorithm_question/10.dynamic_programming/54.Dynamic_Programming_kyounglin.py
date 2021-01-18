# 2021-01-18

# 1,2,3 더하기

# https://www.acmicpc.net/problem/9095

# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1

#정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

n=int(input())
array=[]
for i in range(n):
    array.append(int(input()))


d=[0]*11
d[1]=1
d[2]=2
d[3]=4

for j in array:
    for i in range(4,j+1):
        d[i]=d[i-1]+d[i-2]+d[i-3]

    print(d[j],end='\n')
