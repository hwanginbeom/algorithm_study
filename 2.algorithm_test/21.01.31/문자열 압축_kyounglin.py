# 2021-02-01

# 문자열 압축

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/60057


example=input()


def solution(example):
    answer = 1000000
    check_list = []
    check = []
    for cut in range(1, len(example) // 2 + 2): # 여기서 2는 문자열이 한자리인 경우
        slice = example[0:cut]
        count = 1
        result = ''
        for j in range(cut, len(example) + cut, cut): # 문자열이 1이면 cut도 1 for문 1,1,1은 말이 안됨. 그러므로 cut만큼 더 더해주어야 함
            if slice == example[j:j + cut]:
                count += 1
            else:
                if count == 1:
                    result += slice
                else:
                    result += str(count) + slice
                slice = example[j:cut + j]
                count = 1
        answer = min(answer, len(result))

    return answer

print(solution(example))