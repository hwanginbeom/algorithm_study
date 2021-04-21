# Two Pointer
# 같이 눈사람 만들래?
# https://www.acmicpc.net/problem/20366

N = int(input())
arr = sorted(list(map(int, input().split())))

# 눈사람 키 차이 최댓값으로 설정
diff = 10 ** 9
for start in range(N):
    # end 의 범위는 최소 start 보다 3 커야 하므로
    for end in range(start + 3, N):
        # 내부 start, end 지정
        in_start, in_end = start + 1, end - 1
        #
        while in_start < in_end:
            tmp_diff = (arr[start] + arr[end]) - (arr[in_start] + arr[in_end])
            # 눈사람 키 차이 최솟값으로 갱신
            if abs(tmp_diff) < abs(diff):
                diff = abs(tmp_diff)
            # tmp 값이 0보다 작으면 내부 end 를 줄여서 tmp 값 증가시키기
            # 내부 end 가 내부 start 와 가까워져서 같아지면 while 문을 나와
            # 다음 end 값으로 넘어가므로 이 경우에도 tmp 값은 커진다.
            if tmp_diff < 0: in_end -= 1
            # 반대의 경우 내부 start 를 증가
            else: in_start += 1
print(diff)
