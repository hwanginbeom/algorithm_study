import sys
input = sys.stdin.readline

T = int(input()) # T:테스트케이스
for _ in range(T):
    n = int(input()) # n:지원자의수
    score = []
    for _ in range(n):
        score.append(list(map(int, input().split()))) # a:서류심사성적, b:면접성적
    score = sorted(score, key = lambda x : x[0])

    # 인덱스 번호 높아질수록 서류심사순위가 큰거니까 면접순위는 작아야된다
    num = score[0][1]
    count = 1
    for i in range(1, len(score)):
        if score[i][1] < num:
            num = score[i][1]
            count += 1
        else:
            pass
    print(count)


# 시간초과
#
# import sys
# input = sys.stdin.readline
#
# T = int(input()) # T:테스트케이스
# for _ in range(T):
#     n = int(input()) # n:지원자의수
#     score = []
#     for _ in range(n):
#         score.append(list(map(int, input().split()))) # a:서류심사성적, b:면접성적
#     score = sorted(score, key = lambda x : x[0])
#
#     answer = []
#     for i in range(len(score)-1):
#         for j in range(i+1, len(score)):
#             if score[i][1] < score[j][1]:
#                 answer.append(score[j])
#     print(n - len(set(map(tuple, answer))))


