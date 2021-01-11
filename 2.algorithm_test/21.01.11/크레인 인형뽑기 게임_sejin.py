# def solution(board, moves):
#     answer = 0
#     list = []
#
#     #for문
#         #???? 맨 위에를 어떻게 뽑을까????
#
#         # print(list)
#         if (len(list) >= 2) and (list[len(list)-1] == list[len(list)-2]) :
#             list.pop()
#             list.pop()
#             answer += 1
#     return answer*2
#
# print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

for i in moves :
    for j in range(len(board)) :
        print(i,j)
