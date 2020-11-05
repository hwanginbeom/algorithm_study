# 1, 2
# 숫자 개수 입력
n = int(input())

# 숫자를 저장할 리스트 생성
n_list = []

for i in range(n) :
    num = int(input())
    n_list.append(num)

# 정렬 내장함수 사용
n_list.sort()

for i in n_list :
    print(i)


# 번외 문제
# 숫자 입력
n = int(input())

# 숫자의 각 자리수를 저장할 리스트 생성
n_list = []

# 숫자의 길이. 몇자리 수인지 저장 (문자열 변환)
n_length = len(str(n))

for i in range(n_length) :
    # 가장 높은 자리수의 몫을 구하여 리스트에 삽입
    n_list.append(n // (10 ** (n_length - i - 1)))

    # 그 나머지를 다시 변수에 저장한다.
    n = n % (10 ** (n_length - i - 1))

# print(n_list)

# 내림차순 옵션 적용
n_list.sort(reverse = True)

# 새로운 수를 저장할 변수
new_n = ''
for i in n_list :
    new_n += str(i)

print(int(new_n))
