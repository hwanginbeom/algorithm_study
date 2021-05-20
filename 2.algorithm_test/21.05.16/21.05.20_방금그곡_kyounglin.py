# 2021-05-20

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/17683

# 방금 그곡

m = "ABCDEFG"
musicinfos = ["11:50,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]


# m='CC#BCC#BCC#BCC#B'
# musicinfos=["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
# m='ABC'
# musicinfos=["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]


def solution(m, musicinfos):
    # #치환
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('A#', 'a').replace('G#', 'g')
    check = []
    for i in musicinfos:
        check.append(list(i.split(',')))

    answer = []

    for i in range(len(check)):
        time1 = list(map(int, check[i][0].split(':')))
        time2 = list(map(int, check[i][1].split(':')))
        time = (time2[0] * 60 + time2[1]) - (time1[0] * 60 + time1[1])
        # #치환
        melody = check[i][3].replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('A#', 'a').replace('G#','g')
        if len(melody) <= time:
            idx = 1
            count = 0
            while count < 1440:  # 하루는 1440분이므로 곡의 길이가 1440보다 클수는 없음
                melody1 = melody * idx
                count = len(list(melody1))
                if m in melody1:
                    answer.append((time, i, check[i][2]))
                    break

                idx += 1


        # 음악길이보다 재생시간이 짧은경우
        else:
            if len(melody) >= len(m):
                if m in melody[:time]:
                    answer.append((time, i, check[i][2]))
                else:
                    pass
    # 해당하는 음악이 없는경우
    if len(answer) == 0:
        return '(None)'
    else:
        answer.sort(key=lambda x: (-x[0], x[1]))

        return answer[0][2]


print(solution(m, musicinfos))