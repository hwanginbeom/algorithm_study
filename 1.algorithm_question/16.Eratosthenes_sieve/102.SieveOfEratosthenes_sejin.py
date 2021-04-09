import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

while(1):
    n = int(input())

    count = 0
    if n == 0:
        break
    else:
        for j in range(n+1, 2*n+1):
            if is_prime_number(j) == True:
                count += 1
    print(count)
