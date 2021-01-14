# 자신의 등수를 A등으로 예상하였는데 실제 등수가 B등이 될 경우,
# 이 사람의 불만도는 A와 B의 차이 (|A - B|)로 수치화할 수 있다.
# 당신은 N명의 사람들의 불만도의 총 합을 최소로 하면서, 학생들의 등수를 매기려고 한다.
#
# 각 사람의 예상 등수가 주어졌을 때,
# 김 조교를 도와 이러한 불만도의 합을 최소로 하는 프로그램을 작성하시오.

# 학생 수 N을 입력받는다.
N = int(input())

# 예상 등수를 입력받는다.
expected_rank = []
for i in range(N):
    expected_rank.append(int(input()))

# 예상 등수를 오름차순 정렬한다.
expected_rank.sort()

# 예상 등수에서 index 번호 + 1을 뺀 값의 절대값을 모두 더한다.
A = 0
for i in range(N):
    A += abs(expected_rank[i] - i - 1)

print(A)
