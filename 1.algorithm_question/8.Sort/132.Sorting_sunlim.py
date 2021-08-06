n = int(input())

li = []
for _ in range(n):
    word = input()
    li.append([len(word), word])  # 글자길이와 함께 저장
li.sort()

answer = []
pre_output = ''
for i in range(len(li)):
    if pre_output != li[i][1]:
        print(li[i][1])
    pre_output = li[i][1]