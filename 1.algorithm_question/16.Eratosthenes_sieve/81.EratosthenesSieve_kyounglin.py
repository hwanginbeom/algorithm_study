# 2021-02-26

# 출처 : https://www.acmicpc.net/problem/9020

# 골드바흐의 추측

# 1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다.
# 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.
#
# 골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다.
# 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다.
# 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다.
# 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.
#
# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.


from itertools import combinations
import math


# 풀이 1 - 시간 초과 (조합을 사용해서 풀이) 보기답은 맞음
for _ in range(n):
    test=int(input())
    check=[]
    check2=[]
    minus=[]
    answer=[]
    array=[True for i in range(test+1)]
    # 에라토스테네스의 체 알고리즘 수행
    # 2부터 n의 제곱근까지의 모든 수를 확인하여
    for i in range(2,int(math.sqrt(test))+1):
        if array[i]==True: # i가 소수인 경우
            # i를 제외한 i의 모든 배수를 지우기
            j=2
            while i*j<=test:
                array[i*j]=False
                j+=1
    # 모든 소수 출력
    for i in range(2,test+1):
        if array[i]:
            check.append(i)
            check2.append((i, i))

    for i in list(combinations(check,2)):
        check2.append(i)

    for j in check2:
        if sum(j)==test:
            answer.append(j)

    if len(answer)!=1:
        for k in range(len(answer)):
            minus.append(abs(answer[k][0]-answer[k][1]))
            find=minus.index(min(minus))
        print('%d %d' % (answer[find][0],answer[find][1]))
    else:
        print('%d %d' % (answer[0][0],answer[0][1]))

#풀이2 - 런타임 에러.... 구글링 참고 한건디 ㅠㅠ 보기답은 나오는데 ㅠㅠ
# n 이하의 소수 찾기
def prime_list(n):
    array = [True]*n
    for i in range(2,int(math.sqrt(n))+1):
            if array[i]==True: # i가 소수인 경우
                for j in range(i+i,n,i):
                    array[j]=False
                    j+=1
        # 모든 소수 출력
    return [i for i in range(2,n) if array[i]==True]

# n 이하의 소수들 중 합이 n

def prime_sum(n):
    check=prime_list(n)
    idx=max([i for i in range(len(check)) if check[i]<=n/2])
    for i in range(idx,-1,-1):
        for j in range(i,len(check)):
            if check[i]+check[j]==n:
                return [check[i],check[j]]



for _ in range(int(input())):
    test = int(input())
    if test>=4 and test<=10000:
        print(" ".join(map(str,prime_sum(test))))

# 풀이3

# 소수 미리 전부 구하기
import sys
N = 10001
array = [True] * N
def prime_check(N):
    for i in range(2, N):
        if array[i]:
            for j in range(2*i, N, i):
                array[j] = False
prime_check(N)

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    idx = 0
    while True:
        if array[n//2 - idx] and array[n//2 + idx]: # 언젠가 소수 조합이 나옴
            print(n//2 - idx, n//2 + idx)
            break
        idx += 1

# test는 짝수, test의 절반은 무조건 자연수이고, 그 수가 소수면 이상적인 답
# 그 수가 소수가 아니라면, test의 절반에서 가까운 소수의 조합을 찾기