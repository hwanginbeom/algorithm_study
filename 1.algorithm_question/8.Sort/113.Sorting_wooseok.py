# 좌표 압축
# https://www.acmicpc.net/problem/18870
from bisect import *


def solution() :
    n = int(input())
    num_list = list(map(int, input().split()))

    # 처음 딕셔너리 생성
    _dict = {}
    for i in range(n) :
        _dict[i] = num_list[i]

    # 처음에 받았던 리스트는 중복 제거 후 정렬
    num_list = list(set(num_list))
    num_list.sort()

    # 딕셔너리 정렬
    _list = sorted(_dict.items(), key = lambda x : x[1])

    # 정렬한 딕셔너리는 리스트 내부의 튜플형식이므로
    # 다시 딕셔너리 형태로 변환
    temp = {}
    for item in _list :
        temp[item[0]] = item[1]

    # 이진탐색 내부모듈 이용
    # 중복제거한 정렬 리스트를 사용해야 한다. (서로 다른 좌표의 개수 이므로)
    # --> 위에서 중복제거 후 정렬한 이유
    # 중복제거 이전의 인덱스와 값은 정렬된 채로 모두 가지고 있다. -> temp 변수
    answer = []
    for key in temp.keys() :
        idx = bisect_left(num_list, temp[key])
        answer.append((key, idx))

    answer = sorted(answer, key = lambda x : x[0])

    for i in answer :
        print(i[1], end = ' ')


solution()
# 이진 탐색이라니...
