# 크레인 인형뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061


def solution(board, moves):
    answer = 0

    length = len(board)
    board.reverse()
    new_board = []

    for i in range(length):
        temp = []

        for j in range(length):
            if board[j][i] != 0:
                temp.append(board[j][i])
            else:
                new_board.append(temp)
                break
        else:
            new_board.append(temp)

    stack = []
    for move in moves:
        if new_board[move - 1]:
            stack.append(new_board[move - 1].pop())

        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2

    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves))
