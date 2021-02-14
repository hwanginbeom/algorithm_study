#2021-02-09

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/67256

# 키패드 누르기

numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand='right'

# 키패드 거리구하는 함수 만들기 2차원 array만들다가 포기 -> 딕셔너리로 바꿔봄

def dist(number,hand):
    key_pad={'1':(0,0),'2':(0,1),'3':(0,2),
             '4':(1,0),'5':(1,1),'6':(1,2),
             '7':(2,0),'8':(2,1),'9':(2,2),
             '*':(3,0),'0':(3,1),'#':(3,2)}

    number=str(number)
    hand=str(hand)
    x_hand,y_hand=key_pad[hand] # 손 위치
    x_number,y_number=key_pad[number] # 이동해야하는 번호 위치
    return abs(x_hand-x_number)+abs(y_hand-y_number) # x축 y축 거리를 더해야 이동거리를 확인 가능

def solution(numbers,hand):
    result=''
    left_hand,right_hand='*','#'

    for number in numbers:
        if number in [1,4,7]:
            result+='L'
            left_hand=number
        elif number in [3,6,9]:
            result+='R'
            right_hand=number
        else:
            if dist(number,right_hand)>dist(number,left_hand):
                result+='L'
                left_hand=number
            elif dist(number,right_hand)<dist(number,left_hand):
                result+='R'
                right_hand=number
            else:
                if hand=='right':
                    result+='R'
                    right_hand=number
                else:
                    result+='L'
                    left_hand=number
    return result

print(solution(numbers,hand))