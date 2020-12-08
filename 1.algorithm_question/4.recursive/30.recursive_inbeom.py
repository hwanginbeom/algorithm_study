a = int(input())
c = 1


def recursive_function(i, a, c):
    if i > a:
        return c
    c = c * i
    c = recursive_function(i+1, a, c)
    return c


result = recursive_function(1, a, c)

print(result)
