'''
이취코테 p314 실전문제: 만들 수 없는 금액
'''
import time
start_time = time.time() #측정 시작

N = int(input())
coin = list(map(int, input()))

n = int(input())
data = list(map(int, input().split()))
data.sort()

target=1
for x in data:
  if target < x:
    break
  target += x

print(target)

end_time = time.time()
print(f"{end_time - start_time:.5f} sec")#수행 시간 출력