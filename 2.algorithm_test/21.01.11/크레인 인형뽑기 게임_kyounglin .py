# 크레인 인형뽑기 게임

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3

def solution(board, moves):
    answer = 0
    basket = []

    check = []
    for i in range(len(board)):
        box = []
        for j in range(len(board)):
            box.append(board[j][i])

        check.append(box)

    for k in moves:
        # 빈칸일 경우

        if sum(check[k - 1]) == 0:
            continue

        else:
            for q in check[k - 1]:
                if q != 0:
                    a = check[k - 1].index(q)
                    basket.append(check[k - 1][a])
                    break

            del check[k - 1][a]

        if len(basket) >= 2:
            if basket[-2] == basket[-1]:
                answer += 2
                basket.pop()
                basket.pop()

    return answer