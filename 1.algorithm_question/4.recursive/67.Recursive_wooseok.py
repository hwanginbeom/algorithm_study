# 하노이의 탑
def solution() :
    n = int(input())

    def hanoi(circle, from_pos, to_pos, aux_pos):
        if circle == 1:
            print(from_pos, to_pos)
            return

        hanoi(circle - 1, from_pos, aux_pos, to_pos)

        print(from_pos, to_pos)

        hanoi(circle - 1, aux_pos, to_pos, from_pos)

    count = 2 ** n - 1
    print(count)

    if n <= 20 :
        hanoi(n, 1, 3, 2)


solution()
