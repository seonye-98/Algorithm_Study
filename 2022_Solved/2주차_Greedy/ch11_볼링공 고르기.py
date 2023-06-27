'''
이취코테 p315 실전문제: 볼링공 고르기
2019 SW 마에스트로 입학 테스트
'''
import time
import itertools

M, N = map(int, input().split())
weights = list(map(int, input().split()))

start_time = time.time() #측정 시작

weights.sort()
print(weights)

result = list(itertools.combinations(weights, 2))

for item in result:
  if item[0] == item[1]:
    result.remove(item)

print(len(result))

print("time :", time.time() - start_time)