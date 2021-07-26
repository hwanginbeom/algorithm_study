def solution(places):
    answer = [];

    # place를 하나씩 확인
    for p in places:

        # 거리두기가 지켜지지 않음을 확인하면 바로 반복을 멈추기 위한 key
        key = False;
        nowArr = [];

        # 이번 place를 nowArr에 담아줍니다.
        for n in p:
            nowArr.append(list(n));

        # 이중 for문을 이용해 하나씩 확인합니다.
        for i in range(5):
            if key:
                break;

            for j in range(5):
                if key:
                    break;

                # 사람을 찾아내면 판단을 시작합니다.
                if nowArr[i][j] == "P":

                    if i + 1 < 5:
                        # 만약 바로 아랫부분에 사람이 존재하면 break
                        if nowArr[i + 1][j] == "P":
                            key = True;
                            break;
                        # 만약 아랫부분이 빈테이블이고 그 다음에 바로 사람이 있다면 한칸 떨어져 있더라도 맨허튼 거리는 2이므로 break
                        if nowArr[i + 1][j] == "O":
                            if i + 2 < 5:
                                if nowArr[i + 2][j] == "P":
                                    key = True;
                                    break;
                    # 바로 오른쪽 부분에 사람이 존재하면 break
                    if j + 1 < 5:
                        if nowArr[i][j + 1] == "P":
                            key = True;
                            break;
                        # 만약 오른쪽 부분이 빈테이블이고 그 다음에 바로 사람이 있다면 한칸 떨어져 있더라도 맨허튼 거리는 2이므로 break
                        if nowArr[i][j + 1] == "O":
                            if j + 2 < 5:
                                if nowArr[i][j + 2] == "P":
                                    key = True;
                                    break;
                    # 우측 아래 부분입니다.
                    if i + 1 < 5 and j + 1 < 5:
                        # 만약 우측 아래가 사람이고, 오른 쪽 또는 아랫부분중 하나라도 빈테이블이면 break
                        if nowArr[i + 1][j + 1] == "P" and (nowArr[i + 1][j] == "O" or nowArr[i][j + 1] == "O"):
                            key = True;
                            break;

                    # 좌측 아래부분입니다.
                    if i + 1 < 5 and j - 1 >= 0:
                        # 만약 좌측 아래가 사람이고, 왼쪽 또는 아랫부분중 하나라도 빈테이블이면 break
                        if nowArr[i + 1][j - 1] == "P" and (nowArr[i + 1][j] == "O" or nowArr[i][j - 1] == "O"):
                            key = True;
                            break;

        # 위의 for문동안 key가 True로 변경되었다면 거리두가기 지켜지지 않은것 이므로 0을 answer에 추가
        if key:
            answer.append(0);
        else:
            # key가 false로 끝났다면 거리두기가 지켜졌으므로 1 추가
            answer.append(1);

    # 끝!
    return answer;