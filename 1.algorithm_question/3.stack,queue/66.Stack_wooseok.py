# 좋은 단어
def solution() :
    n = int(input())
    word_list = []

    for _ in range(n) :
        word = list(input())
        word_list.append(word)

    count = 0
    for word in word_list :
        temp = []

        # 단어 맨 뒤부터 하나씩 빼서 비교
        while word :
            if len(temp) >= 2 :
                if temp[-1] == temp[-2] :
                    temp.pop()
                    temp.pop()
            if word :
                temp.append(word.pop())

        # 남아있는 단어 처리
        while True :
            if len(temp) >= 2 :
                if temp[-1] == temp[-2] :
                    temp.pop()
                    temp.pop()
                else :
                    break
            else :
                break

        if not temp :
            count += 1

    print(count)


solution()
