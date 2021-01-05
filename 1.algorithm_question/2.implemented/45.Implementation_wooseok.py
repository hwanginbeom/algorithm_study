# ACM 호텔
import sys


def solution() :
    t = int(sys.stdin.readline())
    room_list = []

    for _ in range(t) :
        h, w, n = map(int, sys.stdin.readline().split())

        # 나누어 떨어지는 경우와 그렇지 않은 경우를 나눠서 계산
        if n % h == 0 :
            front = str(h)
            back = str(n // h)
        else :
            front = str(n % h)
            back = str(n // h + 1)

        # 0 붙이기
        if len(back) == 1 :
            room = front + '0' + back
        else :
            room = front + back

        room_list.append(room)

    for room in room_list :
        print(room)


solution()
