def is_prime_number(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def solution():
    lower = {chr(value): idx + 1 for idx, value in enumerate(list(range(97, 123)))}
    upper = {chr(value): (idx + 27) for idx, value in enumerate(list(range(65, 91)))}
    _dict = {**lower, **upper}
    N = (20 * 52) + 1
    num_list = [1]
    for i in range(2, N):
        if is_prime_number(i) == True:
            num_list.append(i)

    text = input()
    sum = 0
    for i in text:
        sum += _dict[i]
    answer = "It is a prime word." if sum in num_list else "It is not a prime word."
    print(answer)

solution()