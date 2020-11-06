import sys
from collections import Counter

N = int(input())
number = []
for _ in range(N):
    number.append(int(sys.stdin.readline()))


def function1(number):
    result = 0
    result = sum(number)
    result = result / len(number)
    return round(result)


def function2(number):
    result = len(number) // 2
    return number[result]


def function3(numbers):
    if len(numbers) > 1:
        c = Counter(numbers).most_common(2)
        result = (c[1][0] if c[0][1] == c[1][1] else c[0][0])
        return result
    else:
        return numbers[0]


def function4(number):
    result = number[-1] - number[0]
    return result


number.sort()
print(function1(number))
print(function2(number))
print(function3(number))
print(function4(number))