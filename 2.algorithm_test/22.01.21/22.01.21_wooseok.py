# 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256


def solution(numbers, hand):
    answer = ''

    left_pos = '*'
    right_pos = '#'
    num_pos = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2], 0: [3, 1], '*': [3, 0], '#': [3, 2]}

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left_pos = num
        elif num in [3, 6, 9]:
            answer += 'R'
            right_pos = num
        else:
            left_dist = abs(num_pos[left_pos][0] - num_pos[num][0]) + abs(num_pos[left_pos][1] - num_pos[num][1])
            right_dist = abs(num_pos[right_pos][0] - num_pos[num][0]) + abs(num_pos[right_pos][1] - num_pos[num][1])

            if left_dist < right_dist:
                answer += 'L'
                left_pos = num
            elif left_dist > right_dist:
                answer += 'R'
                right_pos = num
            else:
                if hand == 'left':
                    answer += 'L'
                    left_pos = num
                else:
                    answer += 'R'
                    right_pos = num

    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
print(solution(numbers, hand))
