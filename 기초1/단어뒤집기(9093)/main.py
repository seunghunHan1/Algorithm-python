from sys import stdin

tc = int(stdin.readline())


for t in range(tc):
  sentence = list(stdin.readline().split())
  for word in sentence:
    print(word[::-1])
