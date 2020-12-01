import math

n, k = map(int, input().split())

space = n
array = [True for i in range(space + 1)]
number = 0


for i in range(2,space+1):
    if k == number:
        break
    if array[i] == True:
        j =1
        while i * j <= space:
            if array[i*j] == False:
                pass
            else:
                array[i*j] = False
                number += 1
                if k == number:
                    print(i*j)
                    break
            j += 1
