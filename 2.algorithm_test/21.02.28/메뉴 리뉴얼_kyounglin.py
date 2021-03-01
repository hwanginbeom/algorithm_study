# 2021-03-01

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/72411

# 메뉴리뉴얼

from itertools import combinations

#orders=["ABCFG"]
orders=["XYZ", "XWY", "WXA"]
course=[2,3,4]
#course=[2]

# 조합을 이용해서 해결

from itertools import combinations

def solution(orders,course):
    check=[]
    for i in orders:
        array=list(i) #주문한 메뉴조합을 리스트로 만들기
        array.sort() # 리스트를 사전순으로 정렬 - 정렬하지 않으면 조합 했을 경우 xy / yx  별개값으로 나옴
        for j in course: # 코스 종류의 수
            if len(array)>=j: # 코스 종류 수가 주문한 단품 메뉴 조합 보다 크면 안됨 그러므로 코스 종류 수가 크면 무시
                check.append(list(map(''.join,combinations(array,j)))) # 코스 종류 수에 맞게 조합한 리스트를 문자열로 바꾸어 새로운 리스트(check)에 담음
            else:
                pass
    answer=[]
    for i in course:
        count_check = []
        for j in check:
            if len(j[0])==i: # 예를들어 course[2,3,4] 일때 nC2/nC3/nC4 - nC2/nC3/nC4 이런식으로 담겨져 있어서 2는 2끼리 3은 3끼리 비교해서 많은 주문조합수를 구하기 위해 조건문 적용
                for k in j: # 같은 주문조합의 수 끼리 비교하기 위한 리스트가 count_check
                    count_check.append(k)
        index=list(set(count_check)) # 조합에서 중복된 값들을 제거 해서 index로 만듬
        value=[(i,count_check.count(i)) for i in index] # count_check에서 index 에 맞는 값들의 수를 구함 - 많은 단품메뉴 조합을 구하기 위해 튜플로 만듬 ex) ('AB',2) 이런식으로
        value.sort(key=lambda x:-x[1]) # count의 수를 내림차순으로 정리
        for i in value:
            if i[1]==value[0][1] and value[0][1]>=2: # 단품조합은 2개 이상이어야 하고 예를들어 AB :2 AC:2 로 두개가 최대 일때 둘다 가져와야 하므로 조건문을 세움
                answer.append(i[0])
                answer.sort() # 값들을 사전순으로 정리

    return answer


print(solution(orders,course))