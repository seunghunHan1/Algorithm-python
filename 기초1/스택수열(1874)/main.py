from sys import stdin

stack = []
maxCnt = 0
result = []
for t in range(int(stdin.readline())):      
  num = int(stdin.readline())
  if len(stack) == 0:
    maxCnt += 1
    stack.append(maxCnt)
    result.append('+')

  if stack[-1] == num:
    stack.pop()
    result.append('-')
  elif maxCnt > num:
    result = ['NO']    
    break
  else:
    i = 1
    while stack[-1] < num:
      stack.append(maxCnt + i)      
      result.append('+')
      i += 1
    stack.pop()
    result.append('-')
  if num > maxCnt:
    maxCnt = num

for item in result:
  print(item)