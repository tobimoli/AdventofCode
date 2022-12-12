# %%
import os
import string

DAY = str(12)

os.chdir(f'/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day{DAY}')
with open(f"input_day{DAY}.txt", "r") as f:
    DATA = f.read().split("\n")
with open(f"test_day{DAY}.txt", "r") as f:
    TEST = f.read().split("\n")

ALPHABET_DICT = dict(zip(string.ascii_lowercase, list(range(26))))

def compute_height(grid, row, col):
    height = grid[row][col]
    if height == 'S':
        height = 'a'
    elif height == 'E':
        height = 'z'
    height = ALPHABET_DICT[height]
    return height

def is_connecting_node(row, col, old_height, grid):
    n_row, n_col = len(grid), len(grid[0])
    if row >= 0 and row < n_row:
        if col >= 0 and col < n_col:
            new_height = compute_height(grid, row, col)
            if new_height - old_height <= 1:
                return True
    return False

def find_connecting_nodes(grid, row, col):
    nodes = []
    height = compute_height(grid, row, col)
    # get node up, down, left and right from original node.
    for i, j in [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]]:
        if is_connecting_node(i, j, height, grid):
            node = f"{i},{j}"
            nodes.append(node)
    return nodes
    
def make_graph(grid):
    graph = {}
    n_row, n_col = len(grid), len(grid[0])
    for i_row in range(n_row):
        for i_col in range(n_col):
            node = f"{i_row},{i_col}"
            height = grid[i_row][i_col]
            if height == 'S':
                start = node
            elif height == 'E':
                end = node
            possible_nodes = find_connecting_nodes(grid, i_row, i_col)
            graph[node] = dict(zip(possible_nodes, [1] * len(possible_nodes)))
    return graph, start, end

def dijkstra(graph, start):
    nodes = list(graph.keys())
    unvisited = {node: None for node in nodes} #using None as +inf
    visited = {}
    current = start
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour, _ in graph[current].items():
            if neighbour not in unvisited: continue
            newDistance = currentDistance + 1
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        if len(candidates) > 0:
            current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
        else:
            break
    return visited


def read_data(data):
    grid = []
    for line in data:
        grid.append(list(line))
    return grid


def main(data):
    grid = read_data(data)
    graph, s, e = make_graph(grid)
    kortste_pad = dijkstra(graph, s)
    return kortste_pad[e]

def starting_positions(grid):
    lst = []
    n_row, n_col = len(grid), len(grid[0])
    for row in range(n_row):
        for col in range(n_col):
            if compute_height(grid, row, col) == 0:
                node = f"{row},{col}"
                lst.append(node)
    return lst

def main2(data):
    grid = read_data(data)
    graph, _, e = make_graph(grid)
    start_lst = starting_positions(grid)
    kortste_paden = []
    for i, s in enumerate(start_lst):
        print(f"{i} / {len(start_lst)}")
        kortste_pad = dijkstra(graph, s)
        if e in kortste_pad:
            kortste_paden.append(kortste_pad[e])
    return min(kortste_paden)

# part 1
print(main(TEST))
print(main(DATA))

# part 2
print(main2(TEST))
print(main2(DATA))
