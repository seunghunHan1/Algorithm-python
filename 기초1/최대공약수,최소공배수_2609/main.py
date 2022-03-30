from sys import stdin
import math

a, b = map(int, stdin.readline().split())
gcd = math.gcd(a,b)
lcm = int(a*b / gcd)
print(gcd)
print(lcm)
