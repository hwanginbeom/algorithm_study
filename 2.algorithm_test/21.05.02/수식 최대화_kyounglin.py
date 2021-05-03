# 2021-05-03

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/67257



import re
from itertools import permutations

def solution(expression):
    formula_list =permutations(['*','+','-']) # 3가지 수식의 순열 구하기
    answer=0

    for formula in formula_list:
        numbers =re.findall('\d+', expression) # 숫자만 있는 리스트
        operation =re.findall('\W', expression) # 특수문자만 있는 리스트

        for i in formula: # 수식의 종류는 3개
            while i in operation:
                idx=operation.index(i)
                cal=numbers[idx]+operation[idx]+numbers[idx+1]
                numbers[idx]=str(eval(cal)) # eval하면 숫자로 계산 그 뒤 문자로 변환 + str로 변환해야 다음값과 eval 함수로 연산가능
                numbers.pop(idx+1) # 수식을 이용해 계산된 뒷값은 제거 앞에 값은 계산된 값으로 변환됐음
                operation.pop(idx) # 사용한 수식 제거

        cal=abs(int(numbers[-1])) # 최종값은 숫자리스트에서 남는값 + 절대값을 해주어야함

        if cal>answer: # answer보다 크면 answer를 cal로 할당
            answer=cal

    return answer