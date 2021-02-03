# 방 번호
def solution() :
    n = int(input())
    n_list = list(str(n))

    # 한 세트에 9가 2개 들어있는 것과 같은 맥락이므로
    # 6을 9로 바꿔준다. (나중에 개수세는 것이 쉬워지므로)
    for i in range(len(n_list)) :
        if n_list[i] == '6' :
            n_list[i] = '9'

    set_count = 0
    for i in range(10) :
        # 9의 경우에는 한 세트에서 두번 쓸 수 있으므로 2로 나눠준다.
        # 홀수인 경우 나머지까지 더해주면 된다. (짝수는 어차피 0)
        if i == 9 :
            cnt = n_list.count(str(i)) // 2 + n_list.count(str(i)) % 2
        else :
            cnt = n_list.count(str(i))

        if set_count < cnt :
            set_count = cnt

    print(set_count)


solution()
