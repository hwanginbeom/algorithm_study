# 파일명 정렬
# https://programmers.co.kr/learn/courses/30/lessons/17686
# 21.01.07 재풀이


def solution(files):
    answer = []

    file_dict = {}
    index = 0

    for file in files:
        string = ''
        parts = []

        # HEAD 부분 만들기
        while True:
            s = file[0]

            if not s.isdigit():
                string += s
            else:
                break

            file = file[1:]

        parts.append(string.lower())

        string = ''
        cnt = 0

        # NUMBER 부분 만들기
        while cnt < 5:
            s = file[0]

            if s.isdigit():
                string += s
                cnt += 1
            else:
                break

            if len(file) == 1:
                break
            else:
                file = file[1:]

        string = string.lstrip('0')

        if not string:
            string = '0'

        parts.append(int(string))

        # TAIL 추가
        parts.append(file)

        file_dict[index] = parts
        index += 1

    # print(file_dict)

    file_list = sorted(file_dict.items(), key=lambda x: (x[1][0], x[1][1]))

    for i in file_list:
        answer.append(files[i[0]])

    return answer


files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))
