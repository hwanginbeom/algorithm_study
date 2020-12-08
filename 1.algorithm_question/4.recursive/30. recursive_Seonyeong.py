## 10872번: 팩토리얼

# case 1)
def recursive(n):
    if n <= 1:
        return 1
    return n * recursive(n-1)

print(recursive(int(input())))

# case 2)
def repetitive(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

print(repetitive(int(input())))