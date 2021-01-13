n = int(input())

array = []
for _ in range(n) :
    array.append(int(input()))

for i in range(len(array)):
    min_index = i  # 가장 작은(앞쪽) 원소의 인덱스

    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]  # 스와프

for k in range(len(array)) :
    print(array[k])