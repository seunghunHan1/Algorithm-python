from sys import stdin

MAX_NUM = 1000000
map = [False] * (MAX_NUM + 1)
map[1] = True
checked = [False] * (MAX_NUM + 1)
for i in range(2, (MAX_NUM + 1)):
  if map[i] == False:        
    checked[i] = True    
    map[i] = True
    a = i + i
    while True:
      if a > MAX_NUM:
        break
      map[a] = True
      a += i

while True:
  n = int(stdin.readline())
  a = 0
  b = 0  
  if n == 0:
    break
  for i in range(2, n):
    if checked[i] and checked[n - i]:      
      a = i
      b = n-i            
      print(n,'=',a,'+',b)
      break  