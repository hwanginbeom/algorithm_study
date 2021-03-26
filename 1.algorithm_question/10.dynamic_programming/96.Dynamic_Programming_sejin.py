n = input()

array = []
for i in range(0, n + 1):
    if i == 0 or i == 1:
        array.append(1)
    else:
        array.append((array[i - 1] + array[i - 2] * 2) % 10007)

print(array[n] % 10007)
