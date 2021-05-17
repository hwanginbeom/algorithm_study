import datetime

def change(x):
    x = x.replace('A#', 'a').replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g')
    return x

def playtime(x):
    starttime = x[0]
    endtime = x[1]
    totaltime = int((datetime.datetime.strptime(endtime, '%H:%M') - datetime.datetime.strptime(starttime, '%H:%M')).seconds/60)
    return totaltime

def solution(m, musicinfos):
    answer = []

    m = change(m)
    for idx, musicinfo in enumerate(musicinfos):
        musicinfo = change(musicinfo)
        musicinfo = musicinfo.replace('"','').split(',')
        time = playtime(musicinfo)


        if len(musicinfo[3]) >= time :
            melody = musicinfo[3][0:time]
        else:
            a, b = divmod(time, len(musicinfo[3]))
            melody = musicinfo[3] * a + musicinfo[3][0:b]

        if m in melody:
            answer.append([idx, time, musicinfo[2]])

    if len(answer) != 0:
        answer = sorted(answer, key = lambda x: (-x[1], x[0]))
        return answer[0][2]
    return "(None)"