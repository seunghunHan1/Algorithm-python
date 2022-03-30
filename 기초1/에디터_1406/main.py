from sys import stdin

#스택 두개 생성(초기값은 모두 왼쪽 스택에 저장)
left = list(stdin.readline().strip())
right = []

tc = int(stdin.readline())

for t in range(tc):
  l = list(stdin.readline().split())
  if l[0] == 'L':
    if len(left) != 0:
      right.append(left.pop())
  elif l[0] == 'D':
    if len(right) != 0:
      left.append(right.pop())
  elif l[0] == 'B':
    if len(left) != 0:
      left.pop()
  elif l[0] == 'P':
    left.append(l[1])
print(''.join(left + right[::-1]))