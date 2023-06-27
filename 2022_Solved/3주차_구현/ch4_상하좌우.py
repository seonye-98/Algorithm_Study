'''
이취코테 p110 예제문제: 상하좌우
'''
N = int(input())
move = list(input().split())

import time
start_time = time.time() #측정 시작

#동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

curr_pos = [1, 1]

for _move in move:
  tmp_x, tmp_y = curr_pos[0], curr_pos[1]
  if _move == 'R':
    tmp_x += dx[0]
    tmp_y += dy[0]
  elif _move == 'D':
    tmp_x += dx[1]
    tmp_y += dy[1]
  elif _move == 'L':
    tmp_x += dx[2]
    tmp_y += dy[2]
  elif _move == 'U':
    tmp_x += dx[3]
    tmp_y += dy[3]

  if tmp_x < 1 or tmp_x > 5 or tmp_y < 1 or tmp_y > 5:
    pass
  else:
    curr_pos[0] = tmp_x
    curr_pos[1] = tmp_y
  
  #print(_move, curr_pos)

print(curr_pos[0], curr_pos[1])

end_time = time.time()
print(f"{end_time - start_time:.5f} sec")#수행 시간 출력