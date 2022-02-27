#신고 결과 받기

#Dictionary,defaultdict사용

from collections import defaultdict

def solution(id_list, report, k):
    answer=[0]*len(id_list)

    #리포트 리스트의 중복 제거

    report=set(report)

    declare =defaultdict(set) #유저가 신고를 행한 목록//아이디 정보
    declared=defaultdict(int) #유저가 신고를 당한 횟수//신고 횟수 정보
    suspended=[]  #k번 이상 신고당한 유저 목록 //k번 이상이면 게시판이용 정지 시킴

    for r in report:
        do_report,be_reported=r.split()   #do는 신고한 사람, be신고 당한 사람// 각데이터 공백으로 구분
        declared[be_reported]+=1
        declare[do_report].add(be_reported)

        if declared[be_reported] ==k:  #신고를 당해서 K가 된다면 suspenede 저장
            suspended.append(be_reported)


    for s in suspended:   #신고당한 리스트를 돌려서 횟수 측정
        for i in range(len(id_list)):
            if s in declare[id_list[i]]:
                answer[i]+=1

    return answer

