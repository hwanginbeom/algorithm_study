#6주차 복서 정렬하기



#Q. 복서 선수들의 몸무게 weights와 전적을 나타내는 head2head가 매개변수이다.
#복서 선수들의 번호를 다음과 같은 순서로 정렬한 후 return 함수를 완성해라


#1.전체 승률이 높은 복서의 번호가 앞쪽으로 간다. 아직 다른 복서랑 붙어본 적이 없는 복서의 승률은 0%로 취급합니다.
#2.승률이 동일한 복서의 번호들 중에서는 자신보다 몸무게가 무거운 복서를 이긴 횟수가 많은 복서의 번호가 앞쪽으로 갑니다.
#3.자신보다 무거운 복서를 이긴 횟수까지 동일한 복서의 번호들 중에서는 자기 몸무게가 무거운 복서의 번호가 앞쪽으로 갑니다.
#4.자기 몸무게까지 동일한 복서의 번호들 중에서는 작은 번호가 앞쪽으로 갑니다

def solution (weights, head2head):  #매개변수를 담는다.


    player = {i+1:[0.0, 0,weights[i]] for i in range(len(weights))}

    for idx, score in enumerate(head2head):
        cnt=0 #이 부분을 항상 까먹는데!!!중요하다!! 담을그릇이 필요하니깐 잊지마
        for i,s in enumerate(score):
            if s != "N": cnt += 1 #대결횟수 -1
            if s == "W":
                player[idx+1][0]+=1 #승리 횟수+1
                if weights[idx]< weights[i]:
                    player[idx + 1][1] += 1  # 더 무거운 사람 승리 횟수 +1
                player[idx + 1][0] = player[idx + 1][0] / cnt * 100 if cnt != 0 else 0

        player = sorted(player.items(), key=lambda x: (x[1], -x[0]), reverse=True) #람다식에서 기준이 여러개 일때 괄호로 묶어주기
        answer = [i[0] for i in player]
        return answer




