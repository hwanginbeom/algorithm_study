# 2021-07-16

# 거스름돈

n=1000-int(input())
count=0
array=[500,100,50,10,5]

for coin in array:
    count+=n//coin
    n=n%coin

print(count+n) #여기서+n은 1원