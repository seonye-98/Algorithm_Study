import sys
from collections import deque

_input = sys.stdin.readline


def bfs(graph, start, dist):
    queue = deque([start])

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if dist[i] == -1:
                dist[i] = dist[v] + 1
                queue.append(i)


def main():
    n, m, k, x = map(int, _input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        # 도로의 개수
        A, B = map(int, _input().split())
        graph[A].append(B)

    dist = [-1] * (n + 1)
    dist[x] = 0  # 출발 도시까지의 거리는 0으로 설정

    bfs(graph, x, dist)

    check = False
    for i in range(1, n + 1):
        if dist[i] == k:
            print(i)
            check = True

    if not check:
        print(-1)


if __name__ == '__main__':
    main()
