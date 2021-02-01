# 다트 게임
def solution1(dartResult):
    answer = 0

    score_list = []
    cnt = 0
    number = ''

    while cnt < len(dartResult):
        index = dartResult[cnt]

        if index.isdigit():
            number += index
        elif index.isalpha():
            if index == 'S':
                number = int(number) ** 1
            elif index == 'D':
                number = int(number) ** 2
            elif index == 'T':
                number = int(number) ** 3

            if cnt + 1 < len(dartResult):
                if dartResult[cnt + 1] == '#':
                    number *= -1
                elif dartResult[cnt + 1] == '*':
                    number *= 2
                    if score_list:
                        score_list[-1] *= 2
            score_list.append(number)
            number = ''

        cnt += 1

    answer = sum(score_list)

    return answer


dartResult = '1S2D*3T'
# print(solution1(dartResult))



# 문자열 압축
def solution2(s):
    answer = 0
    string = ''

    for n in range(1, len(s) // 2 + 2):
        length = n

        # 문자를 앞에서부터 차례로 n개씩 자르는 로직
        split_list = [s[i:i + length] for i in range(0, len(s), length)]

        new_str = ''
        unit = split_list[0]
        count = 1

        # 비교하는 문자열과 같으면 카운트 1 증가
        # 다른 것이 나오면 새로운 문자열에 카운트와 같이 붙이기
        for i in range(1, len(split_list)):
            if unit == split_list[i]:
                count += 1
            else:
                if count != 1:
                    new_str += str(count)

                new_str += unit

                unit = split_list[i]
                count = 1

        # 남은 문자열 붙여넣기
        if count != 1:
            new_str += str(count)

        new_str += unit

        if n == 1:
            string = new_str
        else:
            if len(string) > len(new_str):
                string = new_str

    answer = len(string)

    return answer


s = "a"
print(solution2(s))
