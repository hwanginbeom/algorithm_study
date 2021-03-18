import sys
input = sys.stdin.readline

# 코드 1.
# +1씩 하면서 k번째 수열의 길이로 break 해서 k번째 수열 뽑기

def count(n):
    k = 0
    while 1:
        k += 1
        x, y = s(k)
        if y >= n:
            break
    return x,y

def s(k):
    if k == 0:
        result = 'moo'
        cnt = 3
    else:
        result = s(k-1)[0] + 'm' + 'o'*(k+2) + s(k-1)[0]
        cnt = len(result)
    return result, cnt

n = int(input())
print(count(n)[0][n-1])


# 코드 2.
# k 자체를 찾아내서 'm'이 나올 인덱스 번호를 뽑아내서 확인하기
#
# n = int(input())
#
# def check_index(n):
#     lst = [0 for i in range(n)]
#     lst[0] = 3
#     if n <= 3:
#         return n
#     for i in range(1,n):
#         lst[i] = 2 * lst[i-1] + (i+3)
#         if lst[i] > n:
#             break
#     return i
#
# def recursive(k):
#     if k == 0:
#         sum = []
#     else:
#         sum = recursive(k-1) + [3,k+3] + recursive(k-1)
#     return sum
#
# answer = [1]
# for j in recursive(check_index(n)):
#     answer.append(answer[-1]+j)
#
# if n in answer:
#     print('m')
# else:
#     print('o')
