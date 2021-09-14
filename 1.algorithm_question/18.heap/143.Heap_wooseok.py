# 중앙값 구하기
# https://www.acmicpc.net/problem/2696
import bisect


def solution() :
    t = int(input())

    for _ in range(t) :
        m = int(input())
        num_list = []

        # 입력
        while True :
            temp_list = list(map(int, input().split()))
            num_list.extend(temp_list)

            if len(temp_list) < 10 :
                break

        answer = []
        queue = []
        for i in range(m) :
            # 정렬된 리스트에 특정 숫자가 들어갈 인덱스에 삽입해주는 함수
            bisect.insort(queue, num_list[i])

            if i % 2 == 0 :
                answer.append(queue[len(queue) // 2])

        print(len(answer))
        for i in range(len(answer)) :
            print(answer[i], end = ' ')
            if i % 10 == 9 or i == len(answer) - 1 :
                print()


solution()
