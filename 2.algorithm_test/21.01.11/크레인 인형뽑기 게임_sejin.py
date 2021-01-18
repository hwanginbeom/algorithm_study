# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves) :
    answer = 0
    list = []

    for i in moves : # i 행
        for j in range(len(board)) : # j 열

            if board[j][i-1] == 0 :
                pass
            else :
                list.append(board[j][i-1])
                board[j][i-1] = 0
                break

        if (len(list) >= 2) and (list[len(list)-1] == list[len(list)-2]) :
            list.pop()
            list.pop()
            answer += 1

    return answer*2

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))