import re
from collections import OrderedDict

def solution(s):
    return list(OrderedDict.fromkeys(sum(sorted(list(list(map(int, i.split(','))) for i in re.split('[{}]+', s) if i not in ('', ',')), key=len), [])))

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
solution(s)
