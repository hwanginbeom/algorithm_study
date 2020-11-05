value_list=[]
value = input()
for i in range(0,int(value)):
    value_list.append( int(input()) )
value_list.sort()
for i in value_list:
    print(i)