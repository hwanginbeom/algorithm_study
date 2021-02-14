# 거리 함수 정의
def distance(position, destination):
    # 현재 위치와 누르고자 하는 번호의 차로 거리 반환
    check = abs(position - destination)
    if check == 0: return int(0)
    elif check in [1, 3]: return int(1)
    elif check in [2, 4, 6]: return int(2)
    elif check in [5, 7, 9]:  return int(3)
    else: return int(4)

def solution(numbers, hand):
    # 초기값 설정
    answer = ''
    pos_L = 10
    pos_R = 12
    # 1,4,7, 3,6,9 누를 경우
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            pos_L = i
        elif i in [3, 6, 9]:
            answer += 'R'
            pos_R = i
        # 2,5,8,0 누를 경우
        else:
            # 0 번을 11로 바꿔 거리 함수에 적용할 수 있게 설정
            if i == 0: i = 11
            # 거리가 가까운 손으로 누르기
            if distance(pos_L, i) < distance(pos_R, i):
                answer += 'L'
                pos_L = i
            elif distance(pos_L, i) > distance(pos_R, i):
                answer += 'R'
                pos_R = i
            else:
                # 거리가 같을 경우
                if hand == 'left':
                    answer += 'L'
                    pos_L = i
                else:
                    answer += 'R'
                    pos_R = i
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
print(solution(numbers, hand))