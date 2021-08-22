# 메뉴 리뉴얼
# https://programmers.co.kr/learn/courses/30/lessons/72411
# 21.02.28 재풀이
import itertools


def solution(orders, course) :
    answer = []

    for i in course :
        menu_dict = {}
        menu_list = []

        # 주문 메뉴들로 부분집합 구하기
        for order in orders :
            order = sorted(list(order))
            temp = list(itertools.combinations(order, i))
            menu_list.extend(temp)

        # 부분집합의 개수 세기
        for menu in menu_list :
            if menu in menu_dict.keys() :
                menu_dict[menu] += 1
            else :
                menu_dict[menu] = 1

        sorted_list = sorted(menu_dict.items(), key = lambda x : x[1], reverse = True)

        # 가장 많은 부분집합 구하기
        if sorted_list :
            max_value = sorted_list[0][1]

            if max_value < 2 :
                continue

            for j in sorted_list :
                if j[1] == max_value :
                    answer.append(''.join(j[0]))

    answer.sort()

    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution(orders, course))
