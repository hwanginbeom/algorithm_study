from collections import Counter

numbers=[]
N = int(input())
for i in range(N):
    numbers.append(input())
# N = 13
# numbers = ['but', 'i', 'wont', 'hesitate', 'no', 'more', 'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']
dict_number = []
numbers = Counter(numbers)
for i in numbers.keys():
    dict_number.append(i)

numbers = dict_number
result = []
numbers.sort()

for i in numbers:
    result.append(len(i))
result = [i[0] for i in sorted(enumerate(result), key=lambda x:x[1])]

for i in result:
    print(numbers[i])



