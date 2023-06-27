"""
백준 : https://www.acmicpc.net/problem/16236
골드3
"""
from collections import deque

n = int(input())
graph = []
fish_pos = []
eat_cnt = 0
shark_pos = ()
shark_w = 2
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for i in range(n):
        if row[i] != 0 and row[i] != 9:
            fish_pos.append((_, i))
        elif row[i] == 9:
            shark_pos = (_, i)

time = 0
shark_x, shark_y = shark_pos[0], shark_pos[1]
graph[shark_x][shark_y] = 0

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)


def bfs(x, y):
    q = deque([(x, y, 0)])
    dist_list = []
    is_visited = [[False] * n for _ in range(n)]
    is_visited[x][y] = True
    min_dist = int(1e9)
    while q:
        x, y, dist = q.popleft()
        print('first', x, y, dist)
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y
            if 0 <= xx < n and 0 <= yy < n and not is_visited[xx][yy]:
                if graph[xx][yy] <= shark_w:
                    is_visited[xx][yy] = True
                    if 0 < graph[xx][yy] < shark_w:
                        print(xx, yy, 'dist', min_dist, dist)
                        min_dist = dist
                        dist_list.append((dist + 1, xx, yy))
                    if dist + 1 <= min_dist:
                        q.append((xx, yy, dist + 1))
    if dist_list:
        dist_list.sort()
        print(dist_list)
        return dist_list[0]
    else:
        return False

    return


fish_cnt = len(fish_pos)

while fish_cnt:
    result = bfs(shark_x, shark_y)
    if not result:
        break
    shark_x, shark_y = result[1], result[2]
    time += result[0]
    eat_cnt += 1
    fish_cnt -= 1
    if shark_w == eat_cnt:
        shark_w += 1
        eat_cnt = 0
    graph[shark_x][shark_y] = 0

print(time)
