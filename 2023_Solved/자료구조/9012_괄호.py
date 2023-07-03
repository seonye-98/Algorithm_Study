'''
https://www.acmicpc.net/problem/9012
난이도 : 실버4
'''
import sys
input = sys.stdin.readline

n = int(input().rstrip()) 


def find_left_prt(left_stack, right_stack):
    while left_stack:
        prt = left_stack.pop()
        if prt == '(':
            break
        else:
            right_stack.append(prt)

for i in range(n):
    check = list(map(str, input().rstrip()))
    left_stack = []
    right_stack = []
    for c in check:
        if c == '(':
            left_stack.append(c)
        elif c == ')':
            if len(left_stack) == 0 :
                right_stack.append(c)
            else:
              find_left_prt(left_stack, right_stack)
        else:
            right_stack.append(c)
    #print(left_stack, right_stack)

    if len(left_stack) != 0 or len(right_stack) != 0:
        print('NO')
    else:
        print('YES')