"""
백준 : https://www.acmicpc.net/problem/14890
골드3
"""


def rotate(_graph):
    return list(zip(*_graph[::-1]))


n, L = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# print(graph)
count = 0
for row in graph:
    is_path = True
    curr = row[0]
    is_step = [False] * n
    for i, h in enumerate(row[1:]):
        if curr == h:
            pass
        elif abs(curr - h) == 1:
            if curr > h:
                # print(curr, h, i, row)
                # print(row[i + 1:i + L + 1] == [h] * L)
                if row[i + 1:i + L + 1] == [h] * L and True not in is_step[i + 1:i + L + 1]:
                    is_step[i + 1:i + L + 1] = [True] * L
                else:
                    is_path = False
                    # print(curr, h, i, row)
                    # print(row[i + 1:i + L + 1], [h] * L)
                    break
            else:
                # print(curr, h, i, row)
                # print(row[i + 1 - L:i + 1] != [h] * L)
                if row[i + 1 - L:i + 1] == [curr] * L and True not in is_step[i + 1 - L:i + 1]:
                    is_step[i + 1 - L:i + 1] = [True] * L
                else:
                    is_path = False
                    # print(curr, h, i, row)
                    # print(row[i + 1 - L:i + 1], [curr] * L)
                    break
        else:
            is_path = False
            break
        curr = h
    if is_path:
        # print(row)
        count += 1
        is_path = False
# print(count)
# print(rotate(graph))
graph = rotate(graph)
# print(graph)
for row in graph:
    is_path = True
    curr = row[0]
    is_step = [False] * n
    for i, h in enumerate(row[1:]):
        if curr == h:
            pass
        elif abs(curr - h) == 1:
            if curr > h:
                # print(curr, h, i, row)
                # print(row[i + 1:i + L + 1] == [h] * L)
                if row[i + 1:i + L + 1] == tuple([h] * L) and True not in is_step[i + 1:i + L + 1]:
                    is_step[i + 1:i + L + 1] = [True] * L
                else:
                    is_path = False
                    # print(curr, h, i, row)
                    # print(row[i + 1:i + L + 1],tuple([h] * L))
                    break
            else:
                # print(curr, h, i, row)
                # print(row[i + 1 - L:i + 1] != [h] * L)
                if row[i + 1 - L:i + 1] == tuple([curr] * L) and True not in is_step[i + 1 - L:i + 1]:
                    is_step[i + 1 - L:i + 1] = [True] * L
                else:
                    is_path = False
                    # print(curr, h, i, row)
                    # print(row[i + 1 - L:i + 1], tuple([curr] * L))
                    break
        else:
            is_path = False
            break
        curr = h
    if is_path:
        # print(row)
        count += 1
        is_path = False
print(count)
