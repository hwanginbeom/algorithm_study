# 2021-03-05

# 출처 : https://www.acmicpc.net/problem/1946

# 언제나 최고만을 지향하는 굴지의 대기업 진영 주식회사가 신규 사원 채용을 실시한다. 인재 선발 시험은 1차 서류심사와 2차 면접시험으로 이루어진다. 최고만을 지향한다는 기업의 이념에 따라 그들은 최고의 인재들만을 사원으로 선발하고 싶어 한다.
#
# 그래서 진영 주식회사는, 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다. 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.
#
# 이러한 조건을 만족시키면서, 진영 주식회사가 이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원수를 구하는 프로그램을 작성하시오.

import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n=int(input())
    score=[]
    cnt=1
    for _ in range(n):
        x,y=map(int,input().split())
        score.append((x,y)) # x는 서류 y는 면접
    score.sort(key=lambda x:x[0])

    max=score[0][1] #초기 면접 점수

    for i in range(1,n):
        if score[i][1]<max: # 이 값보다 작아야함
            cnt+=1
            max=score[i][1]
    print(cnt)