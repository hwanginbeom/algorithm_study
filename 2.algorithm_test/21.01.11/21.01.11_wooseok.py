# 크레인 인형뽑기 게임
def solution1(board, moves):
    answer = 0
    length = len(board)
    new_board = []

    for i in range(length):
        new = []

        for j in range(length - 1, -1, -1):
            if board[j][i] != 0:
                new.append(board[j][i])
            else:
                break

        new_board.append(new)

    pocket = []

    for i in moves:
        if new_board[i - 1]:
            pocket.append(new_board[i - 1].pop())

        if len(pocket) >= 2:
            if pocket[-1] == pocket[-2]:
                pocket.pop()
                pocket.pop()
                answer += 2

    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution1(board, moves))


# 실패율
def solution2(N, stages):
    answer = []
    fail_per_dict = {}

    num = len(stages)

    for i in range(1, N + 1) :
        count = stages.count(i)
        if count == 0 :
            fail_per_dict[str(i)] = 0
        else :
            fail_per_dict[str(i)] = count / num

        num -= count

    fail_per_list = sorted(fail_per_dict.items(), key=lambda x: x[1], reverse=True)

    for i in fail_per_list:
        answer.append(int(i[0]))

    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution2(N, stages))
