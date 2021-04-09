# 2021-04-09

# 출처 : https://www.acmicpc.net/problem/4948

# 베르트랑 공준
#
# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
#
# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
#
# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
#
# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.


import sys
input = sys.stdin.readline

# 소수의 리스트 구하기
def prime_list(n):
    prime_list = [True]*n
    for i in range(2,int(n**0.5)+1):
        if prime_list[i]:
            for j in range(i+i,n,i):
                prime_list[j]=False
    return [i for i in range(2,n) if prime_list[i]]

while 1:
    n=int(input())
    if n==0:
        break
    else:
        value=prime_list(2*n+1)
        print(len([i for i in value if i>n]))