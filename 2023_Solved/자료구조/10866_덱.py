'''
https://www.acmicpc.net/problem/10866
난이도 : 실버4
'''
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
d = deque([])

for i in range(n):
    opt = input().split()
    if opt[0] == 'push_front':
        d.appendleft(int(opt[1]))
    elif opt[0] == 'push_back':
        d.append(int(opt[1]))
    elif opt[0] == 'pop_front':
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif opt[0] == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())
    elif opt[0] == 'size':
        print(len(d))
    elif opt[0] == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif opt[0] == 'front':
        if len(d) == 0:
            print(-1)
        else:
            num1 = d.popleft()
            print(num1)
            d.appendleft(num1)
    elif opt[0] == 'back':
        if len(d) == 0:
            print(-1)
        else:
            num2 = d.pop()
            print(num2)
            d.append(num2)