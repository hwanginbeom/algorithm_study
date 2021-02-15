from collections import Counter

n = int(input())

book_list = []
for _ in range(n) :
    book_list.append(input())

counter = Counter(book_list)

answer = [k for k, v in counter.items() if v == max(counter.values())]
answer.sort()

print(answer[0])
