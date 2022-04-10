'''
이취코테 p312 실전문제: 곱하기 혹은 더하기
'''
import time
start_time = time.time() #측정 시작

num_str = input()

result = int(num_str[0])

for num in num_str[1:]:
  result = max(result+int(num), result*int(num))
  #print(num, result)

end_time = time.time()
print(f"{end_time - start_time:.5f} sec")#수행 시간 출력