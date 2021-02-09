numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hands = "right"

# *는 10 0은 11 #은 12로 판단
answer = ''
left = 10
right = 12

def check(which, num) :
    # 우선적으로 거리, 거리 같다면 잡이로~!
    # 우선 뺸 나머지를 확인해서 라인 확인
    a = abs(num - which)
    b,c = divmod(a,3)

    # 같은 라인 아닌 경우 : 이동수 : b+c
    # 같은 라인 인 경우 : 이동수 : b
    return b+c

for num in numbers :

    if num in [1,4,7] : #왼손
        answer += 'L'
        left = num #왼손위치 변경

    elif num in [3,6,9] : #오른손
        answer += 'R'
        right = num #오른손 위치 변경

    else :
        if num == 0 :
            num = 11

        if check(left, num) > check(right, num) :
            answer += 'R'
            right = num
        elif check(left, num) < check(right, num) :
            answer += 'L'
            left = num
        else :
            answer += hands.upper()[0]
            if hands.upper()[0] == 'R' :
                right = num
            else :
                left = num
print(answer)