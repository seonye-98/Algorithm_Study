'''
https://www.acmicpc.net/problem/1966
난이도 : 실버 3
'''
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    p_arr = list(map(int, input().split()))
    priority = deque(zip([i for i in range(n)], p_arr))
    cnt = 0
    while True:
        idx, p = priority.popleft()
        if idx == m and p == max(p_arr):
            cnt += 1
            print(cnt)
            break
        elif idx != m and p == max(p_arr):
            p_arr.remove(p)
            cnt += 1
        else:
            priority.append((idx, p))
        #print(p_arr, list(priority))
            