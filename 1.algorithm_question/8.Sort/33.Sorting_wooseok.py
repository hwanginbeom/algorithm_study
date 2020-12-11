# 시리얼 번호
def serial_sum(x) :
    sum = 0

    for i in x :
        if 'A' <= i <= 'Z' or 'a' <= i <= 'z' :
            continue
        else :
            sum += int(i)

    return sum


def solution1() :
    n = int(input())
    serial = []

    for _ in range(n) :
        serial.append(input())

    serial = sorted(serial, key=lambda x : (len(x), serial_sum(x), x))

    for i in serial :
        print(i)


solution1()
