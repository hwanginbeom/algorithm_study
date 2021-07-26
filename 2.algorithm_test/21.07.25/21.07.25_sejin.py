def possible(x, y):
    if (0 <= x < 5) and (0 <= y < 5):
        return True
    return False

def solution(places):
    answer = []

    for place in places:
        cnt = 0

        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if possible(i, j + 1) and place[i][j + 1] == 'P':
                        cnt = 1
                    elif possible(i, j + 2) and place[i][j + 1] != 'X' and place[i][j + 2] == 'P':
                        cnt = 1
                    elif possible(i + 1, j) and place[i + 1][j] == 'P':
                        cnt = 1
                    elif possible(i + 1, j + 1) and (place[i + 1][j] != 'X' or place[i][j + 1] != 'X') and place[i + 1][
                        j + 1] == 'P':
                        cnt = 1
                    elif possible(i + 2, j) and place[i + 1][j] != 'X' and place[i + 2][j] == 'P':
                        cnt = 1
                    # 아직 이거 이해가 잘안간다 이 조건은..!
                    elif possible(i + 1, j - 1) and (place[i][j - 1] != "X" or place[i + 1][j] != "X") and place[i + 1][
                        j - 1] == "P":
                        cnt = 1
                if cnt != 0:
                    break

        if cnt == 0:
            answer.append(1)
        else:
            answer.append(0)
    return answer
