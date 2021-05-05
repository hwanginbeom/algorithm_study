import sys

def check_paper(width, x, y):
	pivot = arr[x][y]
	for i in range(x, x + width):
		for j in range(y, y + width):
			if pivot != arr[i][j]:
				return [False, -1]
	return [True, pivot]


def make_paper(width, i, j):
	check = check_paper(width, i, j)
	if check[0]:
		count[check[1]] += 1
		return
	else:
		make_paper(width // 3, i, j)
		make_paper(width // 3, i, j + width // 3)
		make_paper(width // 3, i, j + width // 3 * 2)
		make_paper(width // 3, i + width // 3, j)
		make_paper(width // 3, i + width // 3, j + width // 3)
		make_paper(width // 3, i + width // 3, j + width // 3 * 2)
		make_paper(width // 3, i + width // 3 * 2, j)
		make_paper(width // 3, i + width // 3 * 2, j + width // 3)
		make_paper(width // 3, i + width // 3 * 2, j + width // 3 * 2)


N = int(input())
arr = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(N)]

count = {-1: 0, 0: 0, 1: 0}
make_paper(N, 0, 0)

for cnt in count.values():
	print(cnt)
