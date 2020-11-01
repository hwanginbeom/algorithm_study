## 수정중.....
## git push 테스트중

########### 1번 문제

def solution(answers):
    answer = []

    person1 = [1, 2, 3, 4, 5]  # 5개
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 8개
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10개

    point_list = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == person1[i % 5]:
            point_list[0] += 1
        if answers[i] == person2[i % 8]:
            point_list[1] += 1
        if answers[i] == person3[i % 10]:
            point_list[2] += 1

    # [3,7,1]
    maxindex = 0
    print(point_list)
    tie = []

    for q in range(len(point_list)):
        if point_list[q] > point_list[maxindex]:
            maxindex = q
            tie = []
        elif point_list[q] == point_list[maxindex]:
            tie.append(q)

    if len(tie) == 0:
        answer.append(maxindex + 1)
    else:
        for a in tie:
            answer.append(a + 1)
    return answer


print(solution([3, 3, 1, 1, 2, 2, 4, 4, 5, 5,5,1,2,3,5,8 ]))


##### 2번문제

# n = 2 ~ 30

def solution(n, lost, reserve):
    answer = 0

    for r_person in reserve:
        for l_person in lost:
            if r_person == l_person:
                reserve.remove(r_person)

            ## reserve 에만 뺄 게 아니라 lost에도 뺴야된다 !!!!!
            ## 우석 ) intersection

    real_reserve = reserve.copy()
    clothes = n - len(lost)

    for r in real_reserve:
        for i in lost:
            if r - 1 == i:
                answer += 1
                real_reserve.remove(r)
                break
            elif r + 1 == i:
                answer += 1
                real_reserve.remove(r)

    answer = answer + clothes

    return answer

print(solution(3, [3], [1]))
