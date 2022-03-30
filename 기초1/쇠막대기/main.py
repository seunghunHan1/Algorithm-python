from sys import stdin

l = list(stdin.readline().strip())

st1 = []
st2 = []
result = 0
before = ''
for i in l:
  if i == '(':
    st1.append('(')
  elif i == ')' and before == '(':
    st1.pop()
    cc = len(st1) + len(st2)
    result += cc
    st2 = []
  elif i == ')':
    st1.pop()
    st2.append(')')
  before = i

cc = len(st1) + len(st2)
result += cc
print(result)

#여는 괄호는 무조건 스택에 담기

#닫는 괄호 일시
#1. 이전 값이 여는 괄였을 경우 여는괄호 스택에서 pop후 result에 여는괄호 스택 갯수 + 닫는괄호 스택 갯수 덧셈 후 닫는괄호 스택 비우기
#2. 이전 값이 여는 괄호가 아니였을 경우 여는괄호 스택에서 pop후 닫는 괄호에 담기
