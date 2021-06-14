def solution(key, lock):
    m = len(key)
    n = len(lock)

    def rotate_90(arr):  # 시계방향으로 90도 회전
        ro = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                ro[j][m - 1 - i] = arr[i][j]
        return ro

    back_n = 2 * (m - 1) + n

    def check(startX, startY):  # 키와 자물쇠 체크
        background = [[0] * back_n for _ in range(back_n)]
        # key
        for i in range(m):
            for j in range(m):
                background[startX + i][startY + j] = key[i][j]
        # lock
        for i in range(m - 1, m - 1 + n):
            for j in range(m - 1, m - 1 + n):
                background[i][j] += lock[i - (m - 1)][j - (m - 1)]
                if background[i][j] != 1:
                    return False
        return True

    for _ in range(4):
        for i in range(back_n - m + 1):
            for j in range(back_n - m + 1):
                if check(i, j):
                    return True
        key = rotate_90(key)
    return False
