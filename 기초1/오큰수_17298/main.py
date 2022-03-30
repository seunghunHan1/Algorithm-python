from sys import stdin

n = int(stdin.readline())
l = list(map(int, stdin.readline().split()))

result = [-1] * n
st = [0] #스택에는 인덱스 값을 저장

for i in range(1, n):
  while st and l[st[-1]] < l[i]:
    result[st.pop()] = l[i]
  st.append(i)

print(*result)