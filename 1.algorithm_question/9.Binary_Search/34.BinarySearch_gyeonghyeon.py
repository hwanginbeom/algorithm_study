n, m = map(int, (input().split()))
array = [int(input()) for _ in range(n)]


def counter(distance):
    count = 1
    cur_house = array[0]
    for i in range(1, n):
        if cur_house + distance <= array[i]:
            count += 1
            cur_house = array[i]
    return count


array = sorted(array)
start, end = 1, array[-1] - array[0]

while start <= end:
    mid = (start + end) // 2
    if counter(mid) >= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)