### 가장 큰 수

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse=True)
    return str(int("".join(numbers)))

numbers = [3, 30, 34, 5, 9]
solution(numbers)


### H - Index

def solution(citations):
    H_Index = 0
    citations.sort(reverse=True)

    for num in citations:
        h_cnt = 0

        for k in range(len(citations)):
            if citations[k] >= num:
                h_cnt += 1
        if (h_cnt > H_Index) & (h_cnt <= num):
            H_Index = h_cnt
        else:
            continue

    answer = H_Index
    return answer


### 입국심사

def solution(n, time):
    left, right = 1, max(time) * n

    answer = 0
    while left <= right:
        mid = (left+right)//2
        people = 0

        for i in time:
            people += mid//i
            if people >= n:
                break

        if people >= n:
            answer = mid
            right = mid-1
        elif people < n:
            left = mid+1
    return answer


solution(6, [7, 10])