# 재귀함수
# 하노이 탑
# https://www.acmicpc.net/problem/1914

# 옮기는 과정을 출력하는 함수 작성
def hanoi(N):
    # 원판 한개를 옮기는 초기값 설정
    start = '1 3'
    # 1 이하일 때 초기값 출력
    if N <= 1:
        return start
    # N-1 개 원판을 1에서 2로 옮기는 과정, 초기값, 2에서 3으로 옮기는 과정의 규칙으로 문자열 붙이기
    return hanoi(N - 1).translate(str.maketrans('23', '32')) \
           + '\n' + start + '\n' \
           + hanoi(N - 1).translate(str.maketrans('12', '21'))

# 원판의 개수를 입력받아 옮긴 횟수 출력
n = int(input())
print(2 ** n - 1)
# 20 이하일 경우 과정을 출력
if n <= 20:
    print(hanoi(n))