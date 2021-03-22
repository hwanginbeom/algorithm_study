# 2021.03.21

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/64062

# 징검다리 건너기 - 이진탐색 필요는 알겠음....

stones=[2, 4, 5, 3, 2, 1, 4, 2, 5, 1]

k=3

result=0


def solution(stones,k):
    start,end=1,max(stones)
    answer=1
    while start<=end: # 시작값이 끝값보다 크거나 같을때까지
        mid=(start+end)//2 # 중간점
        zero=0 # 징검다리가 연속으로 같은 값의 수
        check=True
        for i in stones:
            if i<mid:
                zero+=1
                if zero==k: # 최대 칸수
                    check=False
                    break
            else:
                zero=0

        if check:
            answer=max(answer,mid)
            start=mid+1
        else:
            end=mid-1

    return answer

print(solution(stones,k))
