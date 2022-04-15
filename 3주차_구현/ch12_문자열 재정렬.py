'''
이취코테 p322 실전문제: 문자열 재정렬
'''
import time

S = input()

start_time = time.time() #측정 시작

alphabet = []
number = []

for _ in range(len(S)):
  if '0' <= S[_] <= '9':
    number.append(int(S[_]))
  elif S[_].isalpha():
    alphabet.append(S[_])

alphabet = sorted(alphabet)
alphabet.append(str(sum(number)))

answer = ''.join(alphabet)

print(answer)

end_time = time.time()
print(f"{end_time - start_time:.5f} sec")#수행 시간 출력