'''
이취코테 p118 실전문제: 게임 개발
'''
import time

N, M = map(int, input().split())
A, B, d = map(int, input().split())
_map = []
for _ in range(N):
  _row = list(map(int, input().split()))
  _map.append(_row)

#print(_map)

start_time = time.time() #측정 시작

#서 남 동 북
dx = [-1, 0, 1, 0] #B : 서쪽으로 떨어진 칸의 개수
dy = [0, 1, 0, -1] #A : 북쪽으로 떨어진 칸의 개수

gone = [(A, B)]
count = 0
while True:
  idx = 3-d % 4
  #print(idx)
  if 0 <= ( A + dy[idx] ) < N and 0 <= ( B + dx[idx] ) < M:
    tmp = (A  + dy[idx],  B + dx[idx])
    if tmp not in gone and _map[tmp[0]][tmp[1]] == 0:
      gone.append(tmp)
      A += dy[idx]
      B += dx[idx]
      count = 0
      #print('가보지 않은 위치로 이동', gone)
    else:
      d -= 1
      count += 1
      #print('1회전', gone)

  else:
    d -= 1
    count += 1
    #print('2회전', gone)

  if count == 4:
    tmp = (A  - dy[idx],  B - dx[idx])
    if _map[tmp[0]][tmp[1]] == 0:
      A -= dy[idx]
      B -= dx[idx]
      count = 0
      #print('네 방향 모두 가본칸 or 바다인 경우 뒤로 이동', gone)
    else:
      #print(tmp, '네 방향 모두 가본칸 or 바다인 경우에 뒤도 바다면 끝', gone)
      break

print(len(gone))

end_time = time.time()
print(f"{end_time - start_time:.5f} sec")#수행 시간 출력