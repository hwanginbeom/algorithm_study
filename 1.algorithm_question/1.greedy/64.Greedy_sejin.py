n = int(input())
plus = []
minus = []
for _ in range(n) :
    m = int(input())
    if m > 0 :
        plus.append(m)
    else :
        minus.append(m)
plus.sort(reverse=True)
minus.sort()

def plus_2(x) :
    return x[0]*x[1]
def minus_2(x) :
    return abs(x[0]*x[1])

if (len(plus)>1) & (len(minus)>1) :
    if plus_2(plus) >= minus_2(minus) :
        print(sum(minus)+plus_2(plus)+sum(plus[2:]))
    else :
        print(sum(plus) + minus_2(minus) + sum(minus[2:]))
elif len(plus)>1 :
    print('true')
    print(sum(minus)+plus_2(plus)+sum(plus[2:]))
elif len(minus)>1 :
    print(sum(plus) + minus_2(minus) + sum(minus[2:]))
else :
    print(sum(plus)+sum(minus))
