#문자가 몇갤까
#https://www.acmicpc.net/problem/7600



import re
def get_word_nums(string):
    string = re.sub(r"[^a-z]", '', string.lower())

    alphabets = list(set(string))
    return len(alphabets)

if __name__ == "__main__":
    while True:
        string = input()
        if string == "#":
            break
        print(get_word_nums(string))

