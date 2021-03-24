s = input()

array = []
for i in range(len(s)):
    array.append(s[i:len(s)])
array = sorted(array)
print(array)