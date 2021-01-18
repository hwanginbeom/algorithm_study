# 비밀지도
# 2진수 리스트 생성 함수
def to_binary(n, arr) :
    map = []

    for i in range(n):
        binary = []
        temp = arr[i]

        # 0 또는 1인 경우
        if temp == 0 or temp == 1 :
            binary.append(temp)
        else :
            while True:
                # 나머지와 몫
                rest = temp % 2
                temp //= 2

                # 계산 과정에서 0 또는 1이 되었을 경우
                if temp == 0 or temp == 1:
                    binary.append(rest)
                    binary.append(temp)
                    break
                else:
                    binary.append(rest)

        # 0을 넣어서 자리수 맞추기
        if len(binary) != n:
            for _ in range(n - len(binary)):
                binary.append(0)

        # 역순 재배열
        binary.reverse()
        map.append(binary)

    return map


def solution1(n, arr1, arr2):
    answer = []

    map01 = to_binary(n, arr1)
    map02 = to_binary(n, arr2)

    # 최종 지도 만들기
    for i in range(n) :
        temp = ''

        for j in range(n) :
            if map01[i][j] == 0 and map02[i][j] == 0 :
                temp += ' '
            else :
                temp += '#'

        answer.append(temp)

    return answer


n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]
# print(solution1(n, arr1, arr2))


# 파일명 정렬
import re


def alpha(file) :
    n = re.findall('\d+', file)[0]
    head = file.split(n)[0].lower()

    return head


def num(file) :
    n = re.findall('\d+', file)[0]
    number = int(n)

    return number


def solution2(files):
    answer = sorted(files, key = lambda x : (alpha(x), num(x)))

    return answer


files = ['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']
# files = ['A-10 Thunderbolt II', 'B-50 Superfortress', 'F-5 Freedom Fighter', 'F-14 Tomcat']
print(solution2(files))
