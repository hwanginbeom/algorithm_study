# 2021-10-13

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/85002

# 위클리 챌린지 - 6주차_복서 정렬하기

#weights=[50,82,75,120]
#head2head=["NLWL","WNLL","LWNW","WWLN"]

weights=[60,70,60]
head2head=["NNN","NNN","NNN"]

def solution(weights, head2head):
    array=[]
    player=0 # 선수 index

    for vs in head2head:
        if vs.count('W')+vs.count('L')!=0:
            percent=vs.count('W')/(vs.count('W')+vs.count('L'))*100 # 승률
        else:
            percent=0 # 두 복서가 한번도 승부를 하지 않았을 때만 있는 경우
        index=[i for i in range(len(vs)) if 'W' in vs[i]] # 누구와 승부 했는지 파악
        win=0 # 이긴 횟수
        for wei in index: # 자기보다 무거운 복서를 이긴 횟수
            if weights[player]<weights[wei]:
                win+=1
        array.append((player+1,percent,win,weights[player]))
        player+=1

    answer=[i[0] for i in sorted(array,key=lambda x:(-x[1],-x[2],-x[3],x[1]))]

    return answer

print(solution(weights, head2head))