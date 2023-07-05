'''
https://www.acmicpc.net/problem/2164
난이도 : 실버4
'''

from collections import deque

n = int(input())
d = deque([i for i in range(1, n+1)][::-1])

while len(d) != 1:
  n1 = d.pop()
  n2 = d.pop()
  d.appendleft(n2)

print(d.pop())

