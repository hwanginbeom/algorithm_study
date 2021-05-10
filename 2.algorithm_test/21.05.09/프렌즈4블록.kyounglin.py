# 2021-05-10

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/17679

# 프렌즈4블록

board =["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
m= 6
n = 6


def solution(m, n, board):
    board = list(map(list, zip(*board)))  # 리스트 형식으로 분리 ex) [['C', 'A', 'A', 'C'],...]

    def friends_pop(check_list):
        cnt = 0
        array = [i[:] for i in check_list]  # ex) [['C', 'A', 'A', 'C'],...]
        for i in range(1, n):  # i-1 j-1을 위해 인덱스 1부터 for문이 돌아감
            for j in range(1, m):
                if check_list[i][j] == -1: continue
                if check_list[i][j] == check_list[i - 1][j - 1] == check_list[i - 1][j] == check_list[i][
                    j - 1]:  # 정사각형으로 4블록이 같을때
                    array[i][j], array[i - 1][j - 1], array[i - 1][j], array[i][j - 1] = 0, 0, 0, 0  # 0으로 변환

        for i, j in enumerate(array):
            check = j.count(0)
            cnt += check
            array[i] = [-1] * check + [k for k in j if k != 0]  # 과거에 0으로 변환된 값들을 -1로 변환

        return array, cnt

    answer = 0
    while True:
        board, cnt = friends_pop(board)
        if cnt == 0:
            return answer
        answer += cnt

    return answer




print(solution(m, n, board))