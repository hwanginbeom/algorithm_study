import sys
input = sys.stdin.readline

n = input().strip()
print('\n'.join(sorted(list( n[-i-1:] for i in range(len(n))))))

