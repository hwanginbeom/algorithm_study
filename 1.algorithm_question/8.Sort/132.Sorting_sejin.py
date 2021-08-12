n = int(input())

data = []
for _ in range(n) :
    data.append(input())

array = list(set(data))

array.sort()

answer = sorted(array, key = lambda x : (len(x)))
print('\n'.join(answer))