# 2021-04-29

# 출처 : https://www.acmicpc.net/problem/4889
#
# 여는 괄호와 닫는 괄호만으로 이루어진 문자열이 주어진다. 여기서 안정적인 문자열을 만들기 위한 최소 연산의 수를 구하려고 한다. 안정적인 문자열의 정의란 다음과 같다.
#
# 빈 문자열은 안정적이다.
# S가 안정적이라면, {S}도 안정적인 문자열이다.
# S와 T가 안정적이라면, ST(두 문자열의 연결)도 안정적이다.
# {}, {}{}, {{}{}}는 안정적인 문자열이지만, }{, {{}{, {}{는 안정적인 문자열이 아니다.
#
# 문자열에 행할 수 있는 연산은 여는 괄호를 닫는 괄호로 바꾸거나, 닫는 괄호를 여는 괄호로 바꾸는 것 2가지이다.


answer=[]

while True:
    stack=[]
    cnt=0
    text=input()
    if '-' in text:
        break

    for i in range(len(text)):
        if not stack and text[i]=='}': # 스택이 비어있을 떼 {로 시작하게 }를 변환하고 1번 변환했다는 횟수를 cnt에 저장
            cnt+=1
            stack.append('{')

        elif stack and text[i]=='}': # { 와 } 만나면 }를 넣지 않고 {를 비움
            stack.pop()
        else:
            stack.append(text[i]) # { 는 스택에 넣기

    cnt+=len(stack)//2 # 스택이 마지막까지 남아있을경우 괄호 2개 중 하나는 변환 필요하므로 나누기 2의 몫을 추가
    answer.append(cnt)


for i in range(len(answer)):
    print(i+1, '. ', answer[i], sep='')
