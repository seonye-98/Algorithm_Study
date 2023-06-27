'''
이취코테 p311 실전문제: 모험가 길드
'''
import time
start_time = time.time() #측정 시작

N = int(input())
_list = list(map(int, input().split()))

_list.sort()

group = 0

count = 0 #현재 그룹에 포함된 모험가 수

for ele in _list:
  count += 1
  if count >= ele:
    group += 1
    count = 0

print(group)

end_time = time.time()
print(f"{end_time - start_time:.5f} sec")#수행 시간 출력