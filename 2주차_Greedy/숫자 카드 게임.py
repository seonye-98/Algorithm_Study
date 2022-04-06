'''
이취코테 p96 실전문제: 숫자 카드 게임
'''
import time
start_time = time.time() #측정 시작


N, M = map(int, input().split())

answer = 0

for _ in range(M):
  element = list(map(int, input().split()))
  min_val = min(element)
  answer = max(min_val, answer)

print(answer)

end_time = time.time()
print(f"{end_time - start_time:.5f} sec")#수행 시간 출력