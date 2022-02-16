# 2022-02-15
# 수열
# 출처 : https://www.acmicpc.net/problem/2559

N,K = map(int,input().split())
array = list(map(int,input().split()))


# 방법 1 -> 시간초과
sum_value = sum(array[:K])
result = [sum_value]

for i in range(1,len(array)-K):
    sum_value = sum(array[i:i+K])
    result.append(sum_value)

print(max(result))



# 방법 2 -> 통과 : 리스트 슬라이싱이 더 오래걸려 시간초과가 난것 같음
sum_value = sum(array[:K])
result = [sum_value]

for i in range(0,len(array)-K):
    sum_value = sum_value + array[i+K] - array[i]
    result.append(sum_value)

print(max(result))