'''
이취코테 p99 실전문제: 1이 될 때까지
'''
import time
start_time = time.time() #측정 시작

N, M = map(int, input().split())

# sol1)
# count = 0

# while N != 1:
#   if N % M == 0:
#     N /= M

#   else:
#     N -= 1
#   count += 1

# print(count)

result = 0

while True:
    # N이 M로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
    target = (N // M) * M
    result += (N - target)
    N = target
    # N이 M보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if N < M:
        break
    # M로 나누기
    result += 1
    N //= M

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (N - 1)
print(result)

end_time = time.time()
print(f"{end_time - start_time:.5f} sec")#수행 시간 출력