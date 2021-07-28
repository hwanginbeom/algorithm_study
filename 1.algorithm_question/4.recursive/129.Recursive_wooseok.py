# 로또
# https://www.acmicpc.net/problem/6603


def solution() :
    while True :
        input_list = list(map(int, input().split()))

        k = input_list[0]
        if k == 0 :
            break

        S = input_list[1:]
        select = [0 for _ in range(k)]

        def dfs(x, cnt) :
            if cnt == 6 :
                # select 요소가 1인 것만 출력
                for i in range(k) :
                    if select[i] :
                        print(S[i], end = ' ')
                print()
                return

            # select 리스트에 1이 6개가 될 때까지 반복
            # 1로 바꾼 요소는 재귀에서 돌아온 후 다시 0으로 바꿔준다.
            for i in range(x, k) :
                select[i] = 1
                dfs(i + 1, cnt + 1)
                select[i] = 0

        dfs(0, 0)
        print()


solution()
