'''
이취코테 p92 실전문제: 큰 수의 법칙
'''
import time
start_time = time.time() #측정 시작


N, M, K = map(int, input().split())
_list = list(map(int, input().split()))
_list = sorted(_list, reverse=True)

_sum = 0

# sol1) 첫번째 풀이
# _K = K
# while K > 0 and M > 0:
#   _sum += _list[0]
#   K -= 1
#   M -= 1
#   if K == 0:
#     _sum += _list[1]
#     K = _K
#     M -= 1

# sol2) Greedy
count = int(M/(K+1))*K
count += M % (K+1)

_sum += count * _list[0]
_sum += (M-count) * _list[1]

print(_sum)

#프로그램 소스코드
end_time = time.time()
print(f"{end_time - start_time:.5f} sec")#수행 시간 출력