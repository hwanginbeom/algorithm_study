def blocks(m, n, board):
    visited = set()
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == board[i-1][j-1] == board[i-1][j] == board[i][j-1] != '_':
                visited |= set([(i,j),(i-1,j-1),(i-1,j),(i,j-1)])

    # 2*2 되는 얘들 1로 표시
    for a, b in visited:
        board[a][b] = 1

    # 1인 애들 '_'로 대체해 맨 앞으로 옮긴다
    for idx, row in enumerate(board):
        tmp = ['_'] * row.count(1)
        board[idx] = tmp + [b for b in row if b!=1]
    return len(visited)

def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*board)))

    while True:
        result = blocks(m, n, board)
        if result == 0:
            return answer
        answer += result
    return answer
