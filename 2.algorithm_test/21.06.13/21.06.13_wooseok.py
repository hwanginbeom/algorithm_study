import copy


def rotateKey(key):
    n = len(key)

    rect = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rect[j][n - 1 - i] = key[i][j]

    return rect


def solution(key, lock):
    answer = True

    lock_length = len(lock)
    key_length = len(key)

    ### 백그라운드 만들기
    # 정사각형인 백그라운드의 가로(세로)길이를 구한 후 0으로 채우기
    back_length = lock_length + (key_length - 1) * 2
    background = [[0 for _ in range(back_length)] for _ in range(back_length)]

    # 백그라운드에서 Lock 이 시작하는 인덱스
    background_lock = key_length - 1

    # 한가운데에 Lock 넣어주기
    for i in range(background_lock, background_lock + lock_length):
        for j in range(background_lock, background_lock + lock_length):
            background[i][j] = lock[i - background_lock][j - background_lock]

    temp = copy.deepcopy(background)

    ### key 넣어보기
    for _ in range(4):
        for i in range(back_length - key_length + 1):
            for j in range(back_length - key_length + 1):
                x, y = 0, 0

                for a in range(i, i + key_length):
                    for b in range(j, j + key_length):
                        temp[a][b] += key[x][y]
                        y += 1
                    x += 1
                    y = 0

                # 확인하기
                isFlag = True

                for a in range(background_lock, background_lock + lock_length):
                    for b in range(background_lock, background_lock + lock_length):
                        if temp[a][b] != 1:
                            isFlag = False
                            temp = copy.deepcopy(background)
                            break
                    if not isFlag:
                        break

                if isFlag:
                    return True

        key = rotateKey(key)

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
