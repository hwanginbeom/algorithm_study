# 2021-04-28

# 출처 : https://www.acmicpc.net/problem/20291


n=int(input())


array=[input().split('.')[1] for _ in range(n)]

# 방법 1 - count 함수는 시간초과 - for문 때문인가....?ㅎ
# answer=[(i,array.count(i)) for i in set(array)]
# answer.sort(key=lambda x:x[0])

# 방법 2 - counter 함수 사용

from collections import Counter
answer=sorted(Counter(array).items(),key=lambda x:x[0]) # 튜플로 반환

for x,y in answer:
    print(x,y)


