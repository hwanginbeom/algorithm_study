# -*- coding: utf-8 -*-

#백준 11643 소인수분해

n=int(input())
    
#분해가 될때까지루프 돌리기
while n !=1:
    for i in range(2, n+1):
        #나눠지면 출력
        #다음을 위해 해당수로 n을 나눠줌
        
        if(n%i==0):
            print(i)
            n=n//i
            break

