# 2021-03-24

# 출처 : https://www.acmicpc.net/problem/3273

# n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다.
# 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.

# 방법1) 조합으로 풀기 - 메모리 초과
n=int(input())
array=list(map(int,input().split()))
x=int(input())

from itertools import combinations

check=list(combinations(array,2))
answer=[]
for i in check:
    answer.append(sum(i))

print(answer.count(x))

# 방법2 - 정답

count=0
interval_sum=0
end=n-1
start=0

array.sort()

while start<end:
    interval_sum=array[start]+array[end]
    if interval_sum==x:
        count+=1
    elif interval_sum<x:
        start+=1
        continue # 아래 건너뜀
    end-=1

print(count)



