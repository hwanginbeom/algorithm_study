# https://programmers.co.kr/learn/courses/30/lessons/17686
def data_num(x) :
    import re
    num = re.findall('\d+', x)
    return num[0]

def data_head(x) :
    num = data_num(x)
    head = x.split(num)[0].lower()
    return head

def solution(files) :
    answer = sorted(files, key = lambda x : (data_head(x), int(data_num(x))))
    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG", "abc123defg123.jpg"]))