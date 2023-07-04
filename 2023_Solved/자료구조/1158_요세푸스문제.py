'''
https://www.acmicpc.net/problem/1158
난이도 : 실버4
'''
import sys
from collections import deque
input = sys.stdin.readline

n, k = list(map(int, input().split()))

person = deque([i for i in range(1, n+1)])
answer = []

while person:
    for _ in range(k-1):
      person.append(person.popleft())

    answer.append(person.popleft())

print(str(answer).replace('[', '<').replace(']','>'))

#리스트로 구현 시간초과
# person = [i for i in range(1, n+1)]
# idx = 2
# answer = [person[idx]]

# while len(answer) != n:
#     cnt = 0
#     while cnt < k:
#         idx += 1
#         if person[idx%len(person)] in answer:
#             pass
#         else:
#             cnt += 1
        
#     idx %= len(person)
#     answer.append(person[idx])
# print('<',end="")
# print(', '.join(list(map(str,answer))),end="")
# print('>')

