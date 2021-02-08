# 2021-02-08

# 출처 : https://www.acmicpc.net/problem/5430

# AC

# 선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다.
# 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.

# 함수 R은 배열에 있는 숫자의 순서를 뒤집는 함수이고, D는 첫 번째 숫자를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

# 함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 숫자를 버리는 함수이다.
# 배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.
#
from collections import deque
t = int(input())
#
for _ in range(t):
    p=str(input())
    n=int(input())
    array=input()
    array=array[1:-1]

    if ',' not in array and array !="":
        num_deque=deque([int(array)])
    elif array!="":
        num_deque=deque(map(int,array.split(',')))
    else:
        num_deque=deque()

    cnt =0 # 리턴의 수 구하기
    error_cnt=0 # 에러 체크하기 0이면 오류 없음

    for i in range(len(p)):
        if p[i] == "R":
            cnt += 1
        else:
            if len(num_deque) == 0: # 빈 deque면 오류 출력해야함
                error_cnt=1
                break

            if cnt % 2 == 0: # 짝수
                num_deque.popleft()
            else: # 홀수
                num_deque.pop()

    if cnt % 2 == 1: # 홀수
        num_deque.reverse()


    if error_cnt!=1:
        print('['+(','.join(map(str,num_deque)))+']')
    else:
        print('error')


