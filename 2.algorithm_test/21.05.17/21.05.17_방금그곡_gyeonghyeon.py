import datetime


def play_time(infomation):
    end_time = datetime.datetime.strptime(infomation[1], '%H:%M')
    start_time = datetime.datetime.strptime(infomation[0], '%H:%M')
    play_hour = str(end_time - start_time).split(':')
    replay_time = int(play_hour[0]) * 60 + int(play_hour[1])
    return replay_time


def vs(song, timeleng):
    if timeleng <= len(song):
        song = song[:timeleng]
    else:
        multi, plus = divmod(timeleng, len(song))
        song = song * multi + song[:plus]
    return song


def solution(m, musicinfos):
    before = []
    answer = []
    ma = -1
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a').replace("E#",
                                                                                                                 'e')
    for i in musicinfos:
        infomation = i.split(',')
        replay_time = play_time(infomation)
        play_song = infomation[3].replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace(
            'A#', 'a').replace("E#", 'e')
        code = vs(play_song, replay_time)
        before.append([replay_time, infomation[2], code])

    for i in before:
        if m in i[2]:
            ma = max(ma, i[0])
            answer.append(i)

    if len(answer) == 0:
        return '(None)'
    else:
        for i in range(len(answer)):
            if ma == answer[i][0]:
                return answer[i][1]


m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))
