array = []
value = str(input())
for z in range(0, len(value)):
    array.append(int(value[z]))

for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
        array[i], array[min_index] = array[min_index], array[i]  # 스와프
result = ''
array.sort(reverse=True)
for i in array:
    result += str(i)
print(result)


