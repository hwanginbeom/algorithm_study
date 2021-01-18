def data_num(x) :
    import re
    num = re.findall('\d+', x)
    return num[0]

def data_head(x) :
    num = data_num(x)
    head = x.split(num)[0].lower()
    return head

def data_number(x) :
    num = data_num(x)
    number = int(num)
    return number


def solution(files) :
    answer = sorted(files, key = lambda x : (data_head(x), data_number(x)))
    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))