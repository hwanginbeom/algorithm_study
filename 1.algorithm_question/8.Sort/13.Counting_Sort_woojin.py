
word_list = []
sorted_word_list = []

for _ in range(int(input())):
   word_list.append(input())

# set 을 통해 중복 제거
set_word_list = set(word_list)

for word in set_word_list:
   sorted_word_list.append((len(word), word))

sorted_word_list.sort()
for word_len, word in sorted_word_list:
   print(word)