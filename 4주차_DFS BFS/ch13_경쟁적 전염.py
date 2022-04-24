from collections import deque

n, k = map(int, input().split())

graph = []  # 전체 보드 정보를 담는 리스트
data = []  # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기 (낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지의 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색(BFS) 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx < n and 0 <= ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])


"""
오답...
n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while s > 0:
    pos = {data[i][j]: [(i, j)] for i in range(n) for j in range(n) if data[i][j] in range(1, k + 1)}

    for virus in list(pos.keys()):
        for v in pos[virus]:
            for i in range(4):
                nx = v[0] + dx[i]
                ny = v[1] + dy[i]
                if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 0:
                    data[nx][ny] = virus

    s -= 1

if 0 <= x - 1 < n and 0 <= y - 1 < n:
    print(data[x - 1][y - 1])
"""