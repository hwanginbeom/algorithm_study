n = int(input())
def nnn(x,num):
    if x != 1 and x != 0:
        num = num * x
        return nnn(x - 1, num)
    elif x == 0:
        return 1
    else:
        return num

print(nnn(n,1))


