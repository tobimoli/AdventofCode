import numpy as np
import sys

sys.setrecursionlimit(1_000_000)

with open("input.txt") as f:
    data = f.read().split("\n")

start = (0, data[0].find("."))
end = (len(data) - 1, data[-1].find("."))

# grid input
g = [list(r) for r in data]
n, m = len(g), len(g[0])

dic = {"^": [(-1, 0)], ">": [(0, 1)], "v": [(1, 0)], "<": [(0, -1)]}
adj4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def adj(cur: tuple, part=1):
    """Find adjacent points where you can go from cur."""
    adjacent = []
    cx, cy = cur
    adjs = adj4
    if (part == 1) and (g[cx][cy] in "^>v<"):
        adjs = dic[g[cx][cy]]
    for dx, dy in adjs:
        nx, ny = cx + dx, cy + dy
        if nx in range(n) and ny in range(m) and g[nx][ny] != "#":
            adjacent.append((nx, ny))
    return adjacent


def dfs(cur, path, pathset, part):
    if cur == end:
        print("Length:", len(path))
        path_lengths.append(len(path))
    for a in adj(cur, part):
        if a not in pathset:
            path.append(a)
            pathset.add(a)

            dfs(a, path, pathset, part)

            pathset.remove(a)
            path.pop(-1)
    return path_lengths


path_lengths = []
dfs(start, [], set(), part=1)
print(max(path_lengths))


# part 2
def find_connections(cur: tuple) -> dict:
    connections = {}
    for path in adj(cur, 2):
        end_connection, length = find_next_connection([cur], path)
        connections[end_connection] = length
    return connections


def find_next_connection(path: list, cur: tuple):
    while len(adj(cur, 2)) == 2:
        prev = path[-1]
        path.append(cur)

        conns = adj(cur, 2)
        next_step = conns[(conns.index(prev) + 1) % 2]

        cur = next_step
    return next_step, len(path)


def simplify_grid_to_graph() -> dict:
    grid = {}
    nodes = {start}
    new_nodes = [start]

    while len(new_nodes) > 0:
        node = new_nodes.pop(0)
        nodes.add(node)
        connections = find_connections(node)
        grid[node] = connections

        for new_node in connections:
            if new_node != end:
                if new_node not in nodes:
                    new_nodes.append(new_node)
    return grid


def dfs2(cur, lengths, pathset):
    if cur == end:
        print("Length:", sum(lengths))
        path_lengths.append(sum(lengths))
    for a in list(graph[cur]):
        if a not in pathset:
            lengths.append(graph[cur][a])
            pathset.add(a)

            dfs2(a, lengths, pathset)

            pathset.remove(a)
            lengths.pop(-1)
    return path_lengths


graph = simplify_grid_to_graph()
graph[end] = {}

path_lengths = []
dfs2(start, [], set())
print(max(path_lengths))
