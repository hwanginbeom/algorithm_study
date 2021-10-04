# dfs 이용하여 이차원 리스트의 블록 모양 리스트 저장 함수
def dfs(i, j, board, visited, empty, n):
    section = []
    stack = [(i, j)]
    while stack:
        x, y = stack.pop()
        if x >= 0 and y >= 0:  # 인덱스 체크
            try:
                if visited[x][y] == False and board[x][y] == n:
                    visited[x][y] = True
                    section.append((x, y))

                    stack.append((x - 1, y))
                    stack.append((x + 1, y))
                    stack.append((x, y - 1))
                    stack.append((x, y + 1))

            except IndexError:
                continue
    empty.append(sorted(section))


# 블록의 위치를 (0,0)을 기준으로 변경하는 함수
def standard_0(b):
    tmp = []
    std_x = b[0][0]
    std_y = b[0][1]
    for x, y in b:
        tmp.append((x - std_x, y - std_y))
    return sorted(tmp)


def solution(game_board, table):
    answer = []
    N = len(game_board)

    visited_board = [list(False for _ in range(N)) for _ in range(N)]
    empty_board = []  # game_board의 빈자리 좌표 리스트

    visited_table = [list(False for _ in range(N)) for _ in range(N)]
    empty_table = []  # table의 블록 좌표 리스트

    # dfs 이용하여 game_board의 빈 자리 좌표 리스트 empty_board에 저장
    for i in range(N):
        for j in range(N):
            if visited_board[i][j] == False and game_board[i][j] == 0:
                dfs(i, j, game_board, visited_board, empty_board, 0)

    # dfs 이용하여 table의 블록 좌표 리스트 empty_table에 저장
    for i in range(N):
        for j in range(N):
            if visited_table[i][j] == False and table[i][j] == 1:
                dfs(i, j, table, visited_table, empty_table, 1)

    # standard 함수 이용하여 empty_table의 블록 좌표를 (0,0) 기준으로 변경 후 blocks에 저장
    blocks = []
    for block in empty_table:
        blocks.append(standard_0(block))

    # 이차원 리스트 한칸씩 돌아보며 맞는 자리 있는지 확인 함수
    def match(block):
        for x in range(N):
            for y in range(N):
                move = []
                for _x, _y in block:
                    new_x = x + _x
                    new_y = y + _y
                    if new_x >= 0 and new_y >= 0:  # 인덱스 체크
                        try:
                            _ = game_board[x + _x][y + _y]  # 인덱스 체크
                            move.append((x + _x, y + _y))
                        except IndexError:
                            break
                    else:
                        break
                if len(block) == len(move) and move in empty_board:  # 맞는 자리 찾음
                    empty_board.remove(move)  # 빈자리 삭제
                    answer.extend(move)
                    return True
        return False

    # 블록 90도 회전 함수
    def rotate_90(block):
        new = []
        for x, y in block:
            new.append((y, N - 1 - x))
        return standard_0(new)

    # 블록 하나씩 맞는 자리 있는지 살펴보고 없으면 회전 후 찾기 반복
    for block in blocks:
        for _ in range(4):
            if match(block) == False:  # 맞는 자리 없음
                block = rotate_90(block)  # 블록 회전
            else:  # 맞는 자리 찾음
                break

    return len(answer)# dfs 이용하여 이차원 리스트의 블록 모양 리스트 저장 함수
def dfs(i, j, board, visited, empty, n):
    section = []
    stack = [(i, j)]
    while stack:
        x, y = stack.pop()
        if x >= 0 and y >= 0:   # 인덱스 체크
            try:
                if visited[x][y] == False and board[x][y] == n:
                    visited[x][y] = True
                    section.append((x,y))

                    stack.append((x-1, y))
                    stack.append((x+1, y))
                    stack.append((x, y-1))
                    stack.append((x, y+1))

            except IndexError:
                continue
    empty.append(sorted(section))

# 블록의 위치를 (0,0)을 기준으로 변경하는 함수
def standard_0(b):
    tmp = []
    std_x = b[0][0]
    std_y = b[0][1]
    for x, y in b:
        tmp.append((x-std_x, y-std_y))
    return sorted(tmp)


def solution(game_board, table):
    answer = []
    N = len(game_board)

    visited_board = [list(False for _ in range(N)) for _ in range(N)]
    empty_board = []    # game_board의 빈자리 좌표 리스트

    visited_table = [list(False for _ in range(N)) for _ in range(N)]
    empty_table = []    # table의 블록 좌표 리스트

    # dfs 이용하여 game_board의 빈 자리 좌표 리스트 empty_board에 저장
    for i in range(N):
        for j in range(N):
            if visited_board[i][j] == False and game_board[i][j] == 0:
                dfs(i, j, game_board, visited_board, empty_board, 0)

    # dfs 이용하여 table의 블록 좌표 리스트 empty_table에 저장
    for i in range(N):
        for j in range(N):
            if visited_table[i][j] == False and table[i][j] == 1:
                dfs(i, j, table, visited_table, empty_table, 1)

    # standard 함수 이용하여 empty_table의 블록 좌표를 (0,0) 기준으로 변경 후 blocks에 저장
    blocks = []
    for block in empty_table:
        blocks.append(standard_0(block))


    # 이차원 리스트 한칸씩 돌아보며 맞는 자리 있는지 확인 함수
    def match(block):
        for x in range(N):
            for y in range(N):
                move = []
                for _x, _y in block:
                    new_x = x+_x
                    new_y = y+_y
                    if new_x >= 0 and new_y >=0:    # 인덱스 체크
                        try:
                            _ = game_board[x+_x][y+_y]  # 인덱스 체크
                            move.append((x+_x, y+_y))
                        except IndexError:
                            break
                    else:
                        break
                if len(block) == len(move) and move in empty_board: # 맞는 자리 찾음
                    empty_board.remove(move)    # 빈자리 삭제
                    answer.extend(move)
                    return True
        return False

    # 블록 90도 회전 함수
    def rotate_90(block):
        new = []
        for x, y in block:
            new.append((y, N-1 - x))
        return standard_0(new)


    # 블록 하나씩 맞는 자리 있는지 살펴보고 없으면 회전 후 찾기 반복
    for block in blocks:
        for _ in range(4):
            if match(block) == False:       # 맞는 자리 없음
                block = rotate_90(block)    # 블록 회전
            else:   # 맞는 자리 찾음
                break

    return len(answer)