data = list(map(int, input().split()))


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        tmp = a % b
        a = b
        b = tmp
        return gcd(a, b)


def lcm(a, b):
    return a * b // gcd(a, b)


print(gcd(data[0], data[1]))
print(lcm(data[0], data[1]))

