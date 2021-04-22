# 2021-04-22

# 출처 : https://www.acmicpc.net/problem/20366

#
# 언니 엘자와 동생 안나에게는 N개의 눈덩이가 있다. 각 눈덩이 i (1 ≤ i ≤ N)의 지름은 Hi 이다. 하나의 눈사람은 두 개의 눈덩이로 구성되며, 눈덩이 하나를 아래에 두고 그 눈덩이보다 크지 않은 다른 눈덩이를 쌓아올리는 방식으로 만들 수 있다. 이때, 눈사람의 키는 두 눈덩이 지름의 합과 같다.
#
# 엘자와 안나는 눈덩이 N개 중 서로 다른 4개를 골라서 눈사람을 각각 1개씩, 총 2개를 만들려고 한다. 두 자매는 두 눈사람의 키의 차이가 작을수록 두 눈사람의 사이가 좋을 것이라고 믿는다. 우리는 엘자와 안나가 가장 사이좋은 두 눈사람을 만들기 위해서 도와주려고 한다.
#
#
#
# 주어진 N개의 눈덩이를 이용하여 만들 수 있는 두 눈사람의 키 차이 중 최솟값을 구하는 프로그램을 작성하시오.


# pypy3 제출

n = int(input())
array = sorted(list(map(int, input().split())))
answer = 10 ** 10

for start in range(n):
    for end in range(start + 1, n):

        snowman1 = array[start] + array[end]  # 눈사람1
        start2 = start
        end2 = n - 1
        while True:

            while start2 == start or start2 == end:
                start2 += 1
            while end2 == start or end2 == end:
                end2 -= 1

            if start2 >= end2:
                break

            snowman2 = array[start2] + array[end2]  # 눈사람2
            if snowman1 < snowman2:
                answer = min(answer, snowman2 - snowman1)
                end2 -= 1
            elif snowman1 >= snowman2:
                answer = min(answer, snowman1 - snowman2)
                start2 += 1
print(answer)