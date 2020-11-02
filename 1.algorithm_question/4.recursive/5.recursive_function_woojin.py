a,b = map(int, input().split() )

if a >= b:
    large = a
    tiny = b
else:
    large = b
    tiny = a


def gcd(big, small):
    if big % small == 0:
        return small
    else:
        return gcd(small, big % small)


def lcm(big, small):
    if big % small == 0:
        return big
    else:
        return gcd(big, small) * (big / gcd(big, small)) * (small / gcd(big, small))


print(gcd(large, tiny))
print(round(lcm(large, tiny)))


