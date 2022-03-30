from sys import stdin
from collections import deque

tc = int(stdin.readline())
que = deque()
for t in range(tc):
  l = list(stdin.readline().split())
  if l[0] == 'push':
    que.append(l[1])
  elif l[0] == 'pop':
    if que:
      print(que.popleft())
    else:
      print(-1)
  elif l[0] == 'size':
    print(len(que))
  elif l[0] == 'empty':
    if que:
      print(0)
    else:
      print(1)
  elif l[0] == 'front':
    if que:
      print(que[0])
    else:
      print(-1)
  elif l[0] == 'back':
    if que:
      print(que[-1])
    else:
      print(-1)