### 문제 1번

cnt = int(input())
numbers = []
for i in range(cnt):
    numbers.append(int(input()))

for i in range(len(numbers)):
    min_index = i

    for j in range(i + 1, len(numbers)):
        if numbers[min_index] > numbers[j]:
            min_index = j
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]  # 스왑


for num in numbers:
    print(num)


### 문제 2번


cnt = int(input())
numbers = []
for i in range(cnt):
    numbers.append(int(input()))

sorted_numbers = sorted(numbers)

for num in sorted_numbers:
    print(num)
