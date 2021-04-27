import sys

input = sys.stdin.readline

n, file = int(input()), {}
for i in range(n):
    filename = input().split()[0].split('.')[1]
    file[filename] = file.get(filename, 0) + 1

for value in sorted(file.items()):
    print(value[0], value[1])