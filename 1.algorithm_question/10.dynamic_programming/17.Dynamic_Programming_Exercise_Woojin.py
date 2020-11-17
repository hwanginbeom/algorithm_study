# 피보나치 2
n= int(input())
matrix = {0:0,1:1}
def fib(n, matrix):
    if n in matrix:
        return matrix[n]
    matrix[n] = fib(n-1, matrix) + fib(n-2, matrix)
    return matrix[n]
print(fib(n, matrix))



# 피보나치 함수

# 메모이제이션
mem0 = [1, 0]
mem1 = [0, 1]

for i in range(2 , 41):
    mem0.append(mem0[i-1] + mem0[i-2])
    mem1.append(mem1[i-1] + mem1[i-2])

for _ in range(int(input())):
    n = int(input())
    print(mem0[n], mem1[n])