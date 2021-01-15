# 숫자 카드 문제
# 숫자 카드는 정수 하나가 적혀져 있는 카드이다.
# 상근이는 숫자 카드 N개를 가지고 있다.
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.
# https://www.acmicpc.net/problem/10815

# Sol1
# 이진 탐색을 사용하여 해결, 시간이 비교적 오래 걸린다.


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return True
    # 중간점의 값보다 타겟값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 타겟값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)


N = int(input())
card = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

card.sort()

for i in target_list:
    if binary_search(card, i, 0, N - 1) is True:
        print(1, end=' ')
    elif binary_search(card, i, 0, N - 1) is None:
        print(0, end=' ')


# Sol2
# 존재하는지 여부를 반복문을 통해 해결

N = int(input())
card = set(map(int, input().split()))
# set 은 되고 list 는 안된다. why?

M = int(input())
target_list = list(map(int, input().split()))

for i in target_list:
    if i in card:
        print(1, end=' ')
    else:
        print(0, end=' ')

