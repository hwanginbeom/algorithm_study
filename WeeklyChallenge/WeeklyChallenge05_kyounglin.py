# 2021-10-07

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/84512

# 위클리 챌린지 - 5주차_모음사전

# AAAAA -> 인덱스 4번째 자리에서 바꿀때 1번
# AAAA -> 인덱스 3번째 자리에서 바꿀때 1X5+1 6번
# AAA -> 인덱스 2번째 자리에서 바꿀때 6X5+1 31번
# AA -> 인덱스 1번째 자리에서 바꿀때 31X5+1 156번
# A -> 인덱스 1번째 자리에서 바꿀때 156X5+1 781번

word = "AAAAE"
# word = "EIO"

def solution(word):
    change = [781,156,31,6,1]
    vowel = {'A' : 0, 'E' : 1, 'I' : 2, 'O' : 3, 'U' : 4}
    answer=0
    i=0
    while len(word)-i>0:
        answer+=(change[i]*vowel[word[i]])+1
        i+=1
    return answer

print(solution(word))

