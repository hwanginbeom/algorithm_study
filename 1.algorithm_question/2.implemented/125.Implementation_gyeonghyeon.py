import sys
input = sys.stdin.readline

while True:
    sum = 0
    text = input().strip()
    text_dict = {}
    if text == '#':
        break
    else:
        for i in text:
            if i.isalpha() and i.lower() not in text_dict.keys():
                sum +=1
                text_dict[i.lower()] = 1
        print(sum)