import sys

input = sys.stdin.readline

def solution(n, n_list):
    n_list_sort =  sorted(list(set(n_list)))
    num_dict = {}
    for idx, value in enumerate(n_list_sort):
        num_dict[value] = num_dict.get(value,idx)
    print(' '.join([str(num_dict[i]) for i in n_list]))

n = int(input())
n_list = list(map(int, input().split()))
solution(n, n_list)