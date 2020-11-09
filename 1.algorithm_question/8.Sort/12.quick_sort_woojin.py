n = int(input())
array = []

for i in range(n):
    x, y = map(int, input().split())
    array.append([x,y])

def quieck_sort(ary):
    if len(ary) <= 1:
        return ary

    pivot = ary[0]
    tail = ary[1:]

    # list comprehension의 다중 if : 묵시적인 and 조건
    left_side = [i for i in tail if i[0] < pivot[0]] + [i for i in tail if i[0] == pivot[0] if i[1] < pivot[1]]
    right_side = [i for i in tail if i[0] > pivot[0]] + [i for i in tail if i[0] == pivot[0] if i[1] > pivot[1]]

    return quieck_sort(left_side) + [pivot] + quieck_sort(right_side)

result = quieck_sort(array)

for j in result:
    print(j[0], j[1], end='\n')