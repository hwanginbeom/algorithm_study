from itertools import product
import copy
def solution(word):
    word_list = ['A', 'E', 'I', 'O', 'U']
    per1 = copy.deepcopy(word_list)
    per2 = [ ''.join(i) for i in list(product((word_list), repeat=2))]
    per3 = [ ''.join(i) for i in list(product((word_list), repeat=3))]
    per4 = [ ''.join(i) for i in list(product((word_list), repeat=4))]
    per5 = [ ''.join(i) for i in list(product((word_list), repeat=5))]
    word_dict = [*per1, *per2, *per3, *per4, *per5]
    final_dict = sorted(word_dict)
    answer = final_dict.index(word) + 1
    return answer

word = "AAAAE"
solution(word)