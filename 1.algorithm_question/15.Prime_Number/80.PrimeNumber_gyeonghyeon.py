import math
import sys
input = sys.stdin.readline
def is_prime_number(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

num_list = []
for i in range(2,100000+1):
    if is_prime_number(i) == True:
        num_list.append(i)

list_prime = []
k = 1
while True:
    a = list(input().strip())
    max_num = 0
    if sum(list(map(int,a))) == 0:
        break
    number = 1
    while number < len(a):
        b = 0
        for i in range(number,len(a)+1):
            prime = int(''.join(a[b:i]))
            if prime in num_list:
                max_num = max(max_num,prime)
            b +=1
        number +=1
        if prime in num_list:
            max_num = max(max_num, prime)
    if 1 < max_num <= 100000:
        list_prime.append(str(max_num))
print('\n'.join(list_prime))