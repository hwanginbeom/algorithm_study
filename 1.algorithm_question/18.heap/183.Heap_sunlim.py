# -*- coding: utf-8 -*-

#최대 힙 구현
#최대 힙은 최소 힙 구현에서 입력되는 수들에 -1만 곱해주면됨







import sys
import heapq

heap = []
n = int(sys.stdin.readline())


for _ in range(n):
  m = int(sys.stdin.readline())
  if m == 0:
    if len(heap) == 0:
      print(0)
    else:
      print((-1)*heapq.heappop(heap))
  else:
    heapq.heappush(heap, (-1)*m)