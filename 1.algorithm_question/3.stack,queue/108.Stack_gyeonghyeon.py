def count(text, cnt):
    cnt += 1
    c = 0
    while text.find("{}") >= 0:
        text = text.replace("{}", "")
    c += text.count("{{")
    text = text.replace("{{", "")
    c += text.count("}}")
    text = text.replace("}}", "")
    c += text.count("}{") * 2
    print(f"{cnt}. {c}")
    return cnt

cnt = 0
while True:
    text = input()
    if text.find('-') >= 0:
        break
    cnt = count(text, cnt)
