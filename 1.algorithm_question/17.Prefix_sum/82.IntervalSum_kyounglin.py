# 2021-03-02

# 출처 : https://www.acmicpc.net/problem/2559

# 수열

# 매일 아침 9시에 학교에서 측정한 온도가 어떤 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 알아보고자 한다.
#
# 예를 들어, 아래와 같이 10일 간의 온도가 주어졌을 때,
# 3 -2 -4 -9 0 3 7 13 8 -3
# 모든 연속적인 이틀간의 온도의 합은 아래와 같다.
# 이때, 온도의 합이 가장 큰 값은 21이다.
#
# 또 다른 예로 위와 같은 온도가 주어졌을 때, 모든 연속적인 5일 간의 온도의 합은 아래와 같으며,
# 이때, 온도의 합이 가장 큰 값은 31이다.
#
# 매일 측정한 온도가 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 계산하는 프로그램을 작성하시오.

import sys
input=sys.stdin.readline

N,K=map(int,input().split())
array=list(map(int,input().split()))

prefix_sum=sum(array[0:K])
max_sum = prefix_sum
i=0
if K==1: # K가 1인 경우도 생각
    print(max(array))
else: # 그 외 K 값들
    while True:
        prefix_sum-=array[i] # 다음스텝을 넘기기 위해
        if i+K>=N: # 리스트 길이보다 크면 멈춰야함
            break
        prefix_sum+=array[i+K]
        if max_sum<prefix_sum:
            max_sum=prefix_sum
        i+=1

    print(max_sum)




