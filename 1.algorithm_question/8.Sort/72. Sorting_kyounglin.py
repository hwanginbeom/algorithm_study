# 2021-02-15

# 출처 : https://www.acmicpc.net/problem/1302

# 정렬 - 베스트셀러

# 김형택은 탑문고의 직원이다. 김형택은 계산대에서 계산을 하는 직원이다.
# 김형택은 그날 근무가 끝난 후에, 오늘 판매한 책의 제목을 보면서 가장 많이 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다.
# 오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.

n=int(input())
array=[]
for _ in range(n):
    array.append(input())


check=set(array)
answer=[]
for i in list(check):
    answer.append((i,array.count(i)))

# 튜플로 정리
answer.sort(key=lambda x:(-x[1],x[0]))
print(answer[0][0])








