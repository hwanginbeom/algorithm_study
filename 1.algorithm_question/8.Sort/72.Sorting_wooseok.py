# 베스트셀러
def solution() :
    n = int(input())
    book_dict = {}

    for _ in range(n) :
        book = input()

        if book in book_dict.keys() :
            book_dict[book] += 1
        else :
            book_dict[book] = 1

    # -를 붙이면 다중 정렬할 경우 내림차순 옵션 적용
    book_list = sorted(book_dict.items(), key = lambda x : (-x[1], x[0]))

    print(book_list[0][0])


solution()
