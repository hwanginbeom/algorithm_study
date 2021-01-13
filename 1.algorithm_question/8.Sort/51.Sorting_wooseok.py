# 수 정렬하기
def solution() :
    n = int(input())

    array = []
    for _ in range(n) :
        array.append(int(input()))

    # 선택정렬
    for i in range(len(array)):
        # 가장 작은 원소의 인덱스
        min_index = i

        for j in range(i + 1, len(array)):
            # 가장 작은 원소가 다른 원소보다 크기가 크다면
            if array[min_index] > array[j]:
                # 그 원소의 인덱스로 변경한다.
                min_index = j

        # 자리 바꾸기 (swap)
        array[i], array[min_index] = array[min_index], array[i]

    for i in array :
        print(i)


solution()
