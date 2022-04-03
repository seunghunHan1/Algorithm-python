import math

list_num = list(map(int, input().split()))

cnt = 0
for i in list_num:
  if i == 1:
    continue
  ccc = False
  for j in range(2, math.ceil(i/2) + 1):
    if i % j == 0:
      ccc = True
      break
  if ccc != True:
    cnt += 1

print(cnt)