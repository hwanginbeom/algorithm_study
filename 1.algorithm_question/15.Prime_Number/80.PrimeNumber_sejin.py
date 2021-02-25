import math

def is_prime_number(x) :
    if x == 1 :
        return False
    elif (2 <= x) and (x <= 100000) :
        for i in range(2, int(math.sqrt(x)) + 1) :
            if x % i == 0 :
                return False
        return True
    else :
        return False


while(1) :
    data = str(input())
    num = 0

    if data == '0' :
        break
    else :
        for i in range(len(data)+1) :
            for j in range(i+1, len(data)+1) :
                if is_prime_number(int(data[i:j])) == True :
                    num = max(num, int(data[i:j]))
    print(num)
