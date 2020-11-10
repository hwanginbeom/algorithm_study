# 1
def solution1() :
    n = int(input())

    word_list = []
    for i in range(n) :
        word = input()
        word_list.append(word)

    # 중복 제거
    word_list = list(set(word_list))

    count = []
    for i in range(len(word_list)) :
        length = len(word_list[i])
        count.append(length)

    dict = {name : value for name, value in zip(word_list, count)}

    sorted_dict = sorted(dict.items(), key = lambda item : item[1])

    for key, value in sorted_dict :
        print(key)


# solution1()



# 2
def solution2() :
    n = int(input())

    li = []

    for i in range(n) :
        input_arg = input()
        a = input_arg.split()[0]
        n = input_arg.split()[1]

        a = int(a)

        li.append((a, n))

    sorted_li = sorted(li, key = lambda item : item[0])

    for key, value in sorted_li :
        print(key, end = ' ')
        print(value)


# solution2()
