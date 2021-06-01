def convert(num, base):
    T='0123456789ABCDEF'
    q,r=divmod(num,base)

    if q==0:
        return T[r]
    else:
        return convert(q,base)+T[r]

def solution(n, t, m, p):
    answer = ''
    num=0
    cnt=0
    while True:
        for i in convert(num,n):
            if len(answer)>=t:
                return answer
            if cnt%m==p-1:
                answer+=i
            cnt+=1
        num+=1