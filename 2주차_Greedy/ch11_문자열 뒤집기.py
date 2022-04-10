'''
이취코테 p313 실전문제: 문자열 뒤집기
'''
import time
from collections import Counter
start_time = time.time() #측정 시작

S = input()

count0 = 0
count1 = 0

if S[0] == '1':
  count0 += 1
else:
  count1 += 1

for i in range(len(S)-1):
  if S[i] != S[i+1]:
    if S[i+1] == '1':
      count0 += 1
    else:
      count1 += 1

print(min(count0, count1))

# 내가 한 풀이도 ok
# S_list = []

# for char in S:
#   S_list.append(char)

# count = 0

# while True:
#   if '0' not in S_list or '1' not in S_list:
#     break
#   idx1 = S.find('01')
#   idx2 = S.find('10')
#   if idx1 == -1 or idx2 == -1:
#     count += 1
#     break

#   if idx1 < idx2:
#     for _ in range(1, idx2-idx1+1):
#       S_list[idx1+_] = '0'
#     count += 1
    
#   else:
#     for _ in range(1, idx1-idx2+1):
#       S_list[idx2+_] = '1'
#     count += 1

#   S = "".join(S_list)
#   print(S, S_list)

# print('count', count)

end_time = time.time()
print(f"{end_time - start_time:.5f} sec")#수행 시간 출력