# 신규 아이디 추천
def solution1(new_id):
    answer = ''

    # 1단계
    new_id = new_id.lower()

    # 2단계
    temp_id = ''
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ['-', '_', '.']:
            temp_id += i

    new_id = temp_id

    # 3단계
    temp_id = ''
    isFlag = False

    for i in new_id :
        if i == '.' :
            isFlag = True
        else :
            if isFlag :
                temp_id += '.'
                isFlag = False
            temp_id += i

    new_id = temp_id

    if new_id :
        # 4단계
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    else :
        # 5단계
        new_id = 'a'

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]

        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # 7단계
    elif len(new_id) <= 2:
        s = new_id[-1]
        new_id += s * (3 - len(new_id))

    answer = new_id

    return answer


new_id = "...!@BaT#*..y.abcdefghijklm"
# print(solution1(new_id))



# 메뉴 리뉴얼
import itertools


def solution2(orders, course):
    answer = []

    for i in course:
        part_list = []

        for order in orders:
            order = list(order)
            order.sort()

            part_list.extend(list(map(''.join, itertools.combinations(order, i))))

        dict = {}
        for part in part_list :
            if part not in dict.keys() :
                dict[part] = 1
            else :
                dict[part] += 1

        dict_list = sorted(dict.items(), key = lambda x : x[1], reverse = True)

        if dict_list :
            max_value = dict_list[0][1]

            if max_value > 1 :
                for j in dict_list :
                    if j[1] == max_value :
                        answer.append(j[0])

    answer.sort()

    return answer


orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
print(solution2(orders, course))

# 시간초과 원인

# 애초에 단품 메뉴들의 모든 부분집합을 만들어놓고
# 그 부분집합을 또 나누어서 orders 와 일일이 비교를 하려했던 것이 시간초과의 원인...
# 위에 말한대로 코드를 짜면 최소 4중 반복문이 나오기 때문에
# 채점에서 두 개의 테스트 케이스는 시간초과이고, 통과된 케이스중에서 최대로 걸린 시간은 53.86ms

# orders 에 포함된 메뉴들만으로 부분집합을 만들고, 개수를 측정하는 것이 훨씬 효율적이다.
# combinations 함수와 not in 함수를 제외해도 2중 반복문밖에 나오지 않는다.
# 테스트 케이스중 최대로 걸린 시간이 2.51ms로, 정말 많이 줄어든다.
