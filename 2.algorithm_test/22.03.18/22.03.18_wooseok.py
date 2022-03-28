# 메뉴 리뉴얼
# https://programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations


def solution(orders, course):
    answer = []

    for c in course:
        menu_dict = {}

        for order in orders:
            # 요소가 정렬된 상태로 조합 구하기
            order = sorted(list(order))
            all_combi_list = list(combinations(order, c))
            all_str_list = [''.join(list(i)) for i in all_combi_list]

            # 주문된 세트의 개수 구하기
            for i in all_str_list:
                if i not in menu_dict.keys():
                    menu_dict[i] = 1
                else:
                    menu_dict[i] += 1

        menu_dict_list = sorted(menu_dict.items(), key=lambda x: -x[1])

        # 가장 많이 주문된 세트 구하기
        if menu_dict_list:
            max_value = menu_dict_list[0][1]

            for i in menu_dict_list:
                if max_value > 1 and max_value == i[1]:
                    answer.append(i[0])
                else:
                    break

    answer.sort()

    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution(orders, course))
