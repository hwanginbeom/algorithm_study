# -*- coding: utf-8 -*-

#수식최대화

from itertools import permutations
from collections import deque

def solution(expression):
    answer = 0
    ops = ["*", "+", "-"]
    
    # 스택 생성
    li = []
    s = 0
    for i, v in enumerate(expression):
        if v in ["*", "+", "-"]:
            li.append(expression[s:i])
            li.append(v)
            s = i + 1
    else:
        li.append(expression[s:])
    
    # expression에 없는 연산자는 ops에서 제거
    for op in ops:
        if op not in expression:
            ops.remove(op)
            
    # ops에 있는 연산자로 구성할 수 있는 모든 우선순위 생성
    primarity = permutations(ops)
    
    for case in primarity: # 최대 6가지의 연산자 우선순위 조합
        stacks = [deque(li), deque()]
        t1 = 1
        for c in case: # 각 경우에서 연산자 처리
            t1 = (t1+1) % 2 # 스택 토글 변수
            t2 = (t1+1) % 2
            while len(stacks[t1]):
                item = stacks[t1].popleft()
                if len(stacks[t2]) and stacks[t2][-1] == c:
                    c = stacks[t2].pop()
                    n = stacks[t2].pop()
                    item = str(eval(str(n)+c+str(item)))
                stacks[t2].append(item)
            
        result = stacks[len(ops)%2].pop()
        result = abs(int(result))
        answer = max(answer, result)
            
    return answer