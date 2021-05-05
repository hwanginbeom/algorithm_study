import sys
N = int(sys.stdin.readline())
numbers, answer = [], [0, 0, 0]

for i in range(N):
    line = list(map(int, sys.stdin.readline().split(' ')))
    numbers.append(line)

def count(start_row, start_col, length):
    if length == 1:
        answer[numbers[start_row][start_col] + 1] += 1
        return

    first = 0
    for i in range(start_row, start_row+length):
        for j in range(start_col, start_col+length):
            if i == start_row and j == start_col:
                first = numbers[i][j]
                continue
            else:
                if numbers[i][j] != first:
                    second_len = int(length/3)
                    for k in range(start_row, start_row + length, second_len):
                        for l in range(start_col, start_col + length, second_len):
                            count(k, l, second_len)
                    return
    answer[first + 1] += 1
count(0, 0, N)
print('\n'.join(map(str,answer)))
