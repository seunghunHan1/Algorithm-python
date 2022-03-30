from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())

que = deque()
result = []
for i in range(1, n+1):
  que.append(i)

while True:
  if len(que) == 0:
    break
  for i in range(k):
    if i == k-1:
      result.append(que.popleft())
    else:
      que.append(que.popleft())
      
print('<' + str(result)[1:-1] + '>')