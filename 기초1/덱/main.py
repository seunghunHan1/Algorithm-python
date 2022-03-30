from sys import stdin
from collections import deque

n = int(stdin.readline())
q = deque()
for t in range(n):
  l = list(stdin.readline().split())
  if l[0] == 'push_front':
    q.appendleft(l[1])
  elif l[0] == 'push_back':
    q.append(l[1])
  elif l[0] == 'pop_front':
    print(q.popleft()) if q else print(-1) #삼항 연산자 같은 거
  elif l[0] == 'pop_back':
    print(q.pop()) if q else print(-1)
  elif l[0] == 'size':
    print(len(q))
  elif l[0] == 'empty':
    print(0) if q else print(1)
  elif l[0] == 'front':
    print(q[0]) if q else print(-1)
  elif l[0] == 'back':
    print(q[-1]) if q else print(-1)
    