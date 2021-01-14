# 정렬 라이브러리

n = int(input())

rank = []
for _ in range(n) :
    rank.append(int(input()))

rank.sort(reverse=False)

real_rank = list(range(1,n+1))

answer = 0
for k in range(len(real_rank)) :
    answer += real_rank[k] - rank[k]

print(answer)


# 계수 정렬
n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

count = [0] * (len(array) + 1)
for i in range(len(array)):
    count[array[i]] += 1

rank = []
for i in range(len(count)):
    for _ in range(count[i]):
        rank.append(i)

real_rank = list(range(1, n + 1))

answer = 0
for k in range(len(real_rank)):
    answer += real_rank[k] - rank[k]

print(answer)