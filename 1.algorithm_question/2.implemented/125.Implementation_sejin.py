import re

while 1:
    data = input()

    if data == '#':
        break
    print(len(set(re.sub('[^A-Z]', '', data.upper()))))