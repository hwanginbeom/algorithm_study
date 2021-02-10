import sys
input = sys.stdin.readline

r, c = map(int, input().split())
nm = [(-1, 0), (0, -1), (1, 0), (0, 1)]
board = [list(input().rstrip()) for _ in range(r)]
alpha = set()
res = 1

def dfs(alpha, count, cur):
    global res
    alpha.add(board[cur[0]][cur[1]])
    for n in nm:
        nx = cur[0]+n[0]
        ny = cur[1]+n[1]
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in alpha:
            alpha.add(board[nx][ny])
            dfs(alpha, count+1, (nx, ny))
            res = max(count+1,res)
            alpha.remove(board[nx][ny])


dfs(alpha, 1, (0, 0))
print(res)