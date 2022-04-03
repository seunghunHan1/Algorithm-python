from sys import stdin

def fac(n):
  if n == 0:
    return 1
  return fac(n-1) * n

a, b = map(int, stdin.readline().split())
cnt = 0
for i in reversed(list(str(int(fac(a) / (fac(a - b) * fac(b)))))):
  if i == '0':
    cnt += 1
  else:
    break
print(cnt)