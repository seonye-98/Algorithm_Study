'''
이취코테 p115 실전문제: 왕실의 나이트
'''
pos = input()

import time
start_time = time.time() #측정 시작

alphabet = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

row = int(pos[1])
col = alphabet.index(pos[0])

print(row, col)

# 우위, 우밑, 밑우, 밑좌, 좌위, 좌밑, 위우, 위좌
dx = [2, 2, 1, -1, -2, -2, 1, -1]
dy = [-1, 1, 2, 2, -1, 1, -2, -2]

count = 0

for i in range(8):
  tmp_x = col + dx[i]
  tmp_y = row + dy[i]
  if 0 < tmp_x < 9 and 0 < tmp_y < 9:
    #print(tmp_y, alphabet[tmp_x])
    count += 1


print(count)

end_time = time.time()
print(f"{end_time - start_time:.5f} sec")#수행 시간 출력

'''
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
'''