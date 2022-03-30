from sys import stdin

tc = int(stdin.readline())
result = []
for t in range(tc):
  l = list(stdin.readline().split())
  if l[0] == 'push':
    result.append(l[1])
  elif l[0] == 'pop':
    if len(result) == 0:
      print(-1)
    else:
      print(result.pop())
  elif l[0] == 'size':
    print(len(result))
  elif l[0] == 'empty':
    if not result:
      print(1)
    else:
      print(0)
  elif l[0] == 'top':
    if not result:
      print(-1)
    else:
      print(result[-1])