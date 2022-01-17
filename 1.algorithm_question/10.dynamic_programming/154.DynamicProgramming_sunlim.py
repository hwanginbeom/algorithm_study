# 백준 2839번   설탕배달

#설탕 무게를 나타내는 N이 입력되면 3키로와 5키로의 설탕 봉지를 나눠 담아 가장 적은 수의 봉지 출력


sugar =int(input())
bag=0

#whlie 반복문으로 bag개수 샌다

while sugar >=0:
    if sugar % 5 == 0 :#5의 배수이면
        bag +=(sugar//5) #5로 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar-=3
    bag+=1 #5의 배수가 될때까지 설탕-3 봉지 +1

else:
    print(-1)