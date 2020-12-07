## 10773번: 제로

k = int(input())

num = []
for _ in range(k):
    i = int(input())
    if i == 0:
        num.pop()
    else:
        num.append(i)

print(sum(num))


    