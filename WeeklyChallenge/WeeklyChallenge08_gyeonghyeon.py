def solution(sizes):
    sizes = list(map(list, zip(*[sorted(size, reverse=True) for size in sizes])))
    return max(sizes[0]) * max(sizes[1])


sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
solution(sizes)