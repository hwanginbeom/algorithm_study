# 베스트 셀러
# https://www.acmicpc.net/problem/1302

# 입력값 받기
n = int(input())
lst = []
for _ in range(n):
    lst.append(input())

# count 를 dictionary 형식으로 생성
count = {}
# 각 책 제목마다 개수를 value 로 입력
for i in lst:
    try: count[i] += 1
    except: count[i] = 1

# value 가 가장 큰 값을 중복없이 answer 에 입력
answer = []
for j in lst:
    if lst.count(j) == max(count.values()) and j not in answer:
        answer.append(j)

answer.sort()
print(answer[0])