# 1431 - 시리얼 번호
a = int(input())
array = []

for i in range(a):
    b = input()
    array.append(b)

# 1번조건
array.sort(key=len)

for i in range(0,len(array)-1):
    # 2번조건
    if len(array[i]) == len(array[i+1]):
        for z in range(i+1, len(array)):
            a = 0
            b = 0
            if len(array[i]) != len(array[z]):
                break
            for j in range(0,len(array[i])):
                if array[i][j].isdigit() == True:
                    a += int(array[i][j])
            for j in range(0,len(array[i])):
                if array[z][j].isdigit() == True:
                    b += int(array[z][j])
            if a > b :
                array[i], array[z] = array[z], array[i]
            # 3번조건
            elif b == a:
                for last in range(0,len(array[i])):
                    if array[i][last] > array[z][last]:
                        array[i], array[z] = array[z], array[i]
                        break
                    elif array[i][last] < array[z][last]:
                        break

for i in array:
    print(i)
