# 1. 에라토스테네스의 체
def solution1() :
    n, k = map(int, input().split())

    array = [True for _ in range(n + 1)]
    count = 0
    result = 0
    isFlag = False

    for i in range(2, len(array) + 1) :
        if array[i] is False :
            continue
        else :
            j = 1

            while i * j <= n :
                if array[i * j] is False :
                    j += 1
                    continue

                # 해당되는 수를 지워준다.
                array[i * j] = False

                # 횟수 1 증가
                count += 1

                # k번째 지운 수일 경우
                if count == k :
                    isFlag = True
                    result = i * j
                    break

                j += 1

            if isFlag :
                break

    print(result)


# solution1()
