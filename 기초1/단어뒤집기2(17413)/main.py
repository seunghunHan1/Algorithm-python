from sys import stdin

l = stdin.readline().strip()

st = ''
result = ''
i = 0 # 반복문을 위한 변수
h = 0 # '<'를 체크하기 위한 변수
while True:
  #반복문 중지 조건
  if i >= len(l):
    break
  
  if l[i] == '<':
    result = result + st[::-1] + '<'
    st = ''
    h = 1
  elif l[i] == '>':
    h = 0
    result += '>'
  elif h == 1:
    result = result + l[i]
  elif l[i] == ' ':
    result = result + st[::-1] + ' '
    st = ''
  else:
    st += l[i]
  i += 1
  
result += st[::-1]
print(result)