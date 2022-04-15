'''
이취코테 p327 실전문제: 뱀

미완성
'''
import time
start_time = time.time() #측정 시작

N = int(input())
K = int(input())
apple = []
for _ in range(K):
  tmp = list(map(int,input().split()))
  apple.append([tmp[0]-1, tmp[1]-1])
L = int(input())
move = {}

for _ in range(L):
  tmp = list(input().split())
  move[tmp[0]] = tmp[1]

start_time = time.time() #측정 시작

_time = 0
start_pos = [0, 0]
end_pos = [0, 0]
idx = 0
#동, 남, 서, 북
dx = [0, 1 , 0, -1]
dy = [1, 0, -1, 0]

print(apple, move)

while True:
  if _time in map(int,move.keys()):
    print('rotate')
    if move[str(_time)] == 'D':
      idx += 1
    elif move [str(_time)] == 'L':
      idx -= 1
  if idx < 0:
    idx = 4+idx
  
  start_pos[0] += dx[idx]
  start_pos[1] += dy[idx]

  if start_pos[0] < 0 or start_pos[0] > N-1 or start_pos[1] < 0 or start_pos[1] > N-1 :
    break
  else:
    if start_pos in apple:
      apple.remove(start_pos)
      _time += 1
    else:
      end_pos[0] += dx[idx]
      end_pos[1] += dy[idx]
  
  print(start_pos, end_pos)
  _time += 1

print(_time)

end_time = time.time()
print(f"{end_time - start_time:.5f} sec")#수행 시간 출력