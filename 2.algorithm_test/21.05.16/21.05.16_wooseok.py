# 방금그곡
# https://programmers.co.kr/learn/courses/30/lessons/17683


# 시간계산 함수
def timeCalculation(start, end):
    start_hour, start_minute = list(map(int, start.split(':')))
    end_hour, end_minute = list(map(int, end.split(':')))

    if end_minute >= start_minute:
        playtime = end_minute - start_minute + (end_hour - start_hour) * 60
    else:
        end_hour -= 1
        playtime = end_minute + 60 - start_minute + (end_hour - start_hour) * 60

    return playtime


# #이 붙어있는 음 치환
def scaleReplace(string) :
    temp = []

    for s in string :
        if s != '#':
            temp.append(s)
        else:
            temp.append(temp.pop().lower())

    return ''.join(temp)


def solution(m, musicinfos):
    answer = ''
    music_list = []

    m = scaleReplace(m)

    for idx, music in enumerate(musicinfos):
        start_time, end_time, name, scale = music.split(',')

        scale = scaleReplace(scale)

        music_len = len(scale)
        playtime = timeCalculation(start_time, end_time)

        # 플레이 시간에 따른 곡 연장 / 삭제
        if playtime > music_len:
            share = playtime // music_len
            rest = playtime % music_len
            music_list.append((idx, scale * share + scale[:rest], playtime))
        elif playtime < music_len:
            music_list.append((idx, scale[:playtime], playtime))
        else:
            music_list.append((idx, scale, playtime))

    # 유사한 음악 찾아내기
    similar = []
    for i in range(len(music_list)):
        if m in music_list[i][1]:
            similar.append(music_list[i])

    # 유사한 음악이 아무것도 없는 경우
    if not similar :
        return '(None)'

    # 플레이타임 비교
    sorted_similar = sorted(similar, key = lambda x : (-x[2], x[0]))
    answer = musicinfos[sorted_similar[0][0]].split(',')[2]

    return answer


m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m, musicinfos))
