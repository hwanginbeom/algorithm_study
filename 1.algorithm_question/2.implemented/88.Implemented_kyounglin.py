# 2021-03-12

# 출처 : https://www.acmicpc.net/problem/1009

# 분산처리

# 재용이는 최신 컴퓨터 10대를 가지고 있다. 어느 날 재용이는 많은 데이터를 처리해야 될 일이 생겨서 각 컴퓨터에 1번부터 10번까지의 번호를 부여하고, 10대의 컴퓨터가 다음과 같은 방법으로 데이터들을 처리하기로 하였다.
# 1번 데이터는 1번 컴퓨터, 2번 데이터는 2번 컴퓨터, 3번 데이터는 3번 컴퓨터, ... ,
#
# 10번 데이터는 10번 컴퓨터, 11번 데이터는 1번 컴퓨터, 12번 데이터는 2번 컴퓨터, ...
#
# 총 데이터의 개수는 항상 ab개의 형태로 주어진다. 재용이는 문득 마지막 데이터가 처리될 컴퓨터의 번호가 궁금해졌다. 이를 수행해주는 프로그램을 작성하라.


n=int(input())

# 방법1) 시간초과
for _ in range(n):
    a,b=map(int,input().split())
    print(int(str(a**b)[-1]))


# 방법2) 하나하나 조건 입력
for _ in range(n):
    a,b = map(int, input().split())
    a=a%10
    if a==1 or a==5 or a==6:
        print(a)
    elif a==0:
        print(10)
    elif a==4 or a==9:
        if (b%2)==1:
            print(a)
        else:
            print((a*a)%10)
    else:
        if (b%4)==0:
            print(int(str(a**4)[-1]))
        else:
            print(int(str(a**(b%4))[-1]))

