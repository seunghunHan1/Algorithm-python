from sys import stdin

def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n

n = int(stdin.readline())
cnt = 0
for i in reversed(list(str(fac(n)))):
  if i == '0':
    cnt += 1
  else:
    break  
print(cnt)