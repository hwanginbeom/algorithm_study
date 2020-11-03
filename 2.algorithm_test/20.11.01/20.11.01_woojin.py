############################################ 1번문제 #########################################

def solution1(answers):
    answer = []

    person1 = [1, 2, 3, 4, 5]  # 5개
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 8개
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10개

    point_list = [0]*3

    for i in range(len(answers)):
        if answers[i] == person1[i % 5]:
            point_list[0] += 1
        if answers[i] == person2[i % 8]:
            point_list[1] += 1
        if answers[i] == person3[i % 10]:
            point_list[2] += 1

    score_leader = max(point_list)

    for i in range(len(point_list)):
        if score_leader  == point_list[i]:
            answer.append(i + 1)
    return answer


answers = [1, 3, 2, 4, 2]
print(solution1(answers))


############################################ 2번문제 #########################################


def solution2(n, lost, reserve):
    answer = 0

    # 여분있는 사람 중 도둑맞은 애들 제외시키기
    for r_person in reserve:
        for l_person in lost:
            if r_person == l_person:
                reserve.remove(r_person)
                lost.remove(l_person)

    real_reserve = reserve.copy()
    clothes = n - len(lost)
    answer = 0

    # 빌려줄 애들 찾기 
    for student in lost:
        if (student - 1) in reserve:
            reserve.remove(student - 1)
            answer += 1
            continue
        elif (student + 1) in reserve:
            reserve.remove(student + 1)
            answer += 1
            continue

    answer = answer + clothes
    return answer

print(solution2(5, [2,4], [1,3,5]))




############################################ 3번문제 #########################################


def solution3(prices):
    answer = []
    
    for i in range(0, len(prices)):
        count = 0
        
        for j in range(i+1, len(prices)):
            count += 1
            
            if prices[i] <= prices[j]:
                continue
            else:
                break
        answer.append(count)
        
    return answer


solution3([1,2,3,2,1])
