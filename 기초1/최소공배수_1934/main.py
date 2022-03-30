from sys import stdin
import math

for tc in range(int(stdin.readline())):
  a, b = map(int, stdin.readline().split())
  print(int(a*b / math.gcd(a, b)))