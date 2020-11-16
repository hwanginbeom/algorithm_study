### Sugar Delivery

n = int(input())
delivery = 0

def dynamic(x,delivery) :
    if x%5 == 0 :
        delivery = x//5
    else :
        while x > 0 :
            x -= 3
            delivery += 1
            if x%5 == 0 :
                delivery += x//5
                break
        if x < 0 :
            delivery = -1

    print(delivery)

dynamic(n, delivery)

### Making One

import sys
input = sys.stdin.readline

n = int(input())
array = [0 for _ in range(n+1)]
array[0] = 0
array[1] = 0

for i in range(2, n+1):
    if (i%3 == 0 and i%2 == 0):
      array[i] = min(array[i//3], array[i//2], array[i-1]) + 1
      continue

    elif (i%3 == 0 and i%2 != 0):
      array[i] = min(array[i//3], array[i-1]) + 1
      continue

    elif (i%3 != 0 and i%2 == 0):
      array[i] = min(array[i//2], array[i-1]) + 1
      continue

    else:
      array[i] = array[i-1] + 1

print(array[n])

