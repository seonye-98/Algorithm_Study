'''
https://www.acmicpc.net/problem/18258
난이도 : 실버4
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())

queue = deque([])

def push(x):
    queue.append(x)

def pop():
    if queue:
        print(queue.popleft())
    else:
        print(-1)

def size():
    print(len(queue))

def empty():
    if queue:
        print(0)
    else:
        print(1)

def front():
    if queue:
        print(queue[0])
    else:
        print(-1)

def back():
    if queue:
        print(queue[-1])
    else:
        print(-1)

for i in range(n):
    opt = input().split()
    if opt[0] == 'push':
        push(int(opt[1]))
    elif opt[0] == 'pop':
        pop()
    elif opt[0] == 'size':
        size()
    elif opt[0] == 'empty':
        empty()
    elif opt[0] == 'front':
        front()
    elif opt[0] == 'back':
        back()