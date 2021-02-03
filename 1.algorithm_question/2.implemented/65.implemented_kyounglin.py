# 2021-02-03

# 출처 : https://www.acmicpc.net/problem/1475

# 방 번호

# 다솜이는 은진이의 옆집에 새로 이사왔다. 다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.
# 다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오.
# (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)

import math
n=list(map(int,(input())))

number=[i for i in range(10)]
answer=[0]*9 # 9번째를 제외하고 리스트 만들기

for i in n:
    if i in [6,9]:
        answer[6]+=0.5
    else:
        answer[i]+=1

# round쓰면 안됨 --> round(2.5)면 결과가 2나옴 / 주의 필요!!!
answer[6]=math.ceil(answer[6])

print(int(max(answer)))

