from sys import stdin

for t in range(int(stdin.readline())):
  stack = []
  sentence = list(stdin.readline())
  error = False
  for i in sentence:
    if i == '(':
      stack.append('(')
    elif i == ')':
      if not stack:
        error = True
        break
      else:
        stack.pop()
  if not stack and not error:
    print('YES')
  else:
    print('NO')
  