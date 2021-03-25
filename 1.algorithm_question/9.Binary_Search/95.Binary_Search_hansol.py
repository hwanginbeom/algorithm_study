# 이진 탐색
# 두 용액
# https://www.acmicpc.net/problem/2470

N = int(input())
# 입력값을 정렬
lst = sorted(list(map(int, input().split())))

# 시작점과 끝점 index 설정
start = 0
end = N - 1
# 결과값의 초기값 설정
result = lst[start] + lst[end]
# 목표값의 index 초기 설정
target_s = start
target_e = end

# 시작점과 끝점을 가운데로 좁혀가면서
while start < end:
    _sum = lst[start] + lst[end]
    # 두 수의 합이 0에 가까우면 result, target 갱신
    if abs(_sum) < abs(result):
        result = _sum
        target_s = start
        target_e = end
        # 0이면 반복문을 종료
        if result == 0:
            break
    # 두 수의 합이 음수면 시작값을 한 단계 큰 값으로
    # 양수면 끝값을 한 단계 작은 값으로 조정하며 반복문 시행
    if _sum < 0:
        start += 1
    else:
        end -= 1

print(lst[target_s], lst[target_e])