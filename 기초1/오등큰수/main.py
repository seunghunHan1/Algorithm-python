from sys import stdin

n = int(stdin.readline())
l = list(map(int, stdin.readline().split()))

result = [-1] * n
st = [0] #스택에는 인덱스 값을 저장
map = [0] * 1000001

for i in l:
  map[i] += 1

for i in range(1, n):  
  while st and map[l[st[-1]]] < map[l[i]]:
    result[st.pop()] = l[i]
  st.append(i)

print(*result)