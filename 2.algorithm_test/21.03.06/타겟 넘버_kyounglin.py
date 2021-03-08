# 2021-03-06

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/43165

# 타겟 넘버

numbers=[1,1,1,1,1]
target=3

stack=[]

# 방법 1) dfs/bfs를 사용하지 않고 완전 탐색
from itertools import product

def solution(numbers,target):
    array=[(x,-x) for x in numbers]
    sum_list=list(map(sum,product(*array))) # 튜플 안에서 product 사용하려면 튜플리스트 앞에 *
    return sum_list.count(target)

print(solution(numbers,target))

# 방법 2) dfs - 트리구조를 생각하기

def dfs_solution(numbers,target):
    result=[0]

    for i in range(len(numbers)):
        array=[]
        for j in range(len(result)):
            array.append(result[j]-numbers[i])
            array.append(result[j]+numbers[i])
        result=array
    return result.count(target)

print(dfs_solution(numbers,target))
