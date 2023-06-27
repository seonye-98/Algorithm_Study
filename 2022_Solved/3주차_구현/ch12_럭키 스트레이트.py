'''
이취코테 p321 실전문제: 럭키 스트레이트

'''
import time

score = input()

start_time = time.time() #측정 시작

left = score[:len(score)//2]
right = score[len(score)//2:]

l_sum, r_sum = 0, 0

for _ in range(len(score)//2):
  l_sum += int(left[_])
  r_sum += int(right[_])

if l_sum == r_sum:
  print('LUCKY')
else:
  print('READY')

end_time = time.time()
print(f"{end_time - start_time:.5f} sec")#수행 시간 출력