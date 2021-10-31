from itertools import permutations


def solution(k, dungeons):
    answer = 0

    for condition in permutations([i for i in range(len(dungeons))]):
        kTemp, ansTemp = k, 0

        for index in condition:
            minimumRequired, consumption = dungeons[index]

            if kTemp >= minimumRequired:
                kTemp -= consumption
                ansTemp += 1

        answer = max(answer, ansTemp)

    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))  # 3