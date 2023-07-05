'''
https://www.acmicpc.net/problem/1935
난이도 : 실버3
'''
import sys
input = sys.stdin.readline

n = int(input())
cal_str = input().rstrip()

alp_num = {}
alp = []
num_arr = []
stack = []

for i in range(n):
    num_arr.append(int(input()))

for s in cal_str:
    if ord(s) in range(ord('A'), ord('Z')+1) and s not in alp:
        alp.append(s)

alp_num = dict(zip(alp, num_arr))

for s in cal_str:
    if ord(s) in range(ord('A'), ord('Z')+1):
        stack.append(alp_num[s])
    else:
        cal = 0
        num2 = stack.pop()
        num1 = stack.pop()
        if s == '+':
            cal = num1 + num2
        elif s == '-':
            cal = num1 - num2
        elif s == '/':
            cal = num1/num2
        elif s == '*':
            cal = num1 * num2
        
        stack.append(cal)
        
print("{:.2f}".format(stack[0]))