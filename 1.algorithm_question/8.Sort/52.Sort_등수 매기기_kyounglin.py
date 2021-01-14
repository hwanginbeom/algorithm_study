# 2021-01-14

# https://www.acmicpc.net/problem/2012

#2007년 KOI에 N명의 학생들이 참가하였다. 경시일 전날인 예비소집일에, 모든 학생들은 자신이 N명 중에서 몇 등을 할 것인지 예상 등수를 적어서 제출하도록 하였다.
# KOI 담당조교로 참가한 김진영 조교는 실수로 모든 학생의 프로그램을 날려 버렸다.
# 1등부터 N등까지 동석차 없이 등수를 매겨야 하는 김 조교는, 어쩔 수 없이 각 사람이 제출한 예상 등수를 바탕으로 임의로 등수를 매기기로 했다.

#자신의 등수를 A등으로 예상하였는데 실제 등수가 B등이 될 경우, 이 사람의 불만도는 A와 B의 차이 (|A - B|)로 수치화할 수 있다.
# 당신은 N명의 사람들의 불만도의 총 합을 최소로 하면서, 학생들의 등수를 매기려고 한다.

# 각 사람의 예상 등수가 주어졌을 때, 김 조교를 도와 이러한 불만도의 합을 최소로 하는 프로그램을 작성하시오.


import sys
input=sys.stdin.readline

n=int(input())
array=[]
for _ in range(n):
    array.append(int(input()))

# 방법 1
array.sort()

predict=[]
for i in range(len(array)):
    predict.append(abs(array[i]-(i+1)))

print(sum(predict))

# 방법2 : 선택 정렬 -> 근데 시간초과 ㅋㅋㅋㅋ

# for i in range(len(array)):
#     for j in range(i,0,-1):
#         if array[j]<array[j-1]:
#             array[j],array[j-1]=array[j-1],array[j]
#         else:
#             break
#
# predict=[]
# for i in range(len(array)):
#     predict.append(abs(array[i]-(i+1)))
#
# print(sum(predict))