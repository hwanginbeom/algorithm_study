n = int(input())
data = list(map(int, input().split()))
data.sort()

rest = 0
sum = 0

if n == 1:
  print(data[0])
else:
  for i in range(n):
    sum += data[i] + rest
    rest += data[i]
print(sum)