'''
https://www.acmicpc.net/problem/10828
난이도 : 실버4
'''
import sys
input = sys.stdin.readline

n = int(input())
stack = []

def push(stack, n):
    stack.append(n)

def pop(stack):
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()
    
def size(stack):
    return len(stack)

def empty(stack):
    if len(stack) == 0:
        return 1
    else:
        return 0
  
def top(stack):
    if len(stack) == 0:
        return -1
    else:
      return stack[-1]

for i in range(n):
    option = input().strip().split()
    if option[0] == 'push':
        push(stack, option[1])
    elif option[0] == 'pop':
        print(pop(stack))
    elif option[0] == 'size':
        print(size(stack))
    elif option[0] == 'empty':
        print(empty(stack))
    elif option[0] == 'top':
        print(top(stack))