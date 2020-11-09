# 1
def quick_sort1(array) :
    # 리스트가 하나 이하의 원소만을 담고 있을 경우 종료
    if len(array) <= 1 :
        return array

    # 첫 번째 원소
    pivot = array[0]
    # 피벗을 제외한 리스트
    tail = array[1:]

    # 분할된 왼쪽 부분
    left_side = [x for x in tail if x[0] < pivot[0]] + [x for x in tail if x[0] == pivot[0] and x[1] < pivot[1]]
    # 분할된 오른쪽 부분
    right_side = [x for x in tail if x[0] > pivot[0]] + [x for x in tail if x[0] == pivot[0] and x[1] > pivot[1]]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에 대해 각각 정렬을 수행하고, 전체 리스트 반환
    return quick_sort1(left_side) + [pivot] + quick_sort1(right_side)


def solution1() :
    n = int(input())

    pos = []
    for i in range(n) :
        x, y = map(int, input().split())
        pos.append([x, y])

    for i in quick_sort1(pos) :
        print(i[0], end = ' ')
        print(i[1])


# solution1()



# 2
def quick_sort2(array) :
    # 리스트가 하나 이하의 원소만을 담고 있을 경우 종료
    if len(array) <= 1 :
        return array

    # 첫 번째 원소
    pivot = array[0]
    # 피벗을 제외한 리스트
    tail = array[1:]

    # 분할된 왼쪽 부분
    left_side = [x for x in tail if x[1] < pivot[1]] + [x for x in tail if x[1] == pivot[1] and x[0] < pivot[0]]
    # 분할된 오른쪽 부분
    right_side = [x for x in tail if x[1] > pivot[1]] + [x for x in tail if x[1] == pivot[1] and x[0] > pivot[0]]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에 대해 각각 정렬을 수행하고, 전체 리스트 반환
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)


def solution2() :
    n = int(input())

    pos = []
    for i in range(n) :
        x, y = map(int, input().split())
        pos.append([x, y])

    for i in quick_sort2(pos) :
        print(i[0], end = ' ')
        print(i[1])


# solution2()
