import numpy as np
import itertools as it

with open("input.txt") as f:
    data = f.read().split("\n")


# create graph with each connection
def create_graph_from_connections(connections, simple=False):
    graph = {}
    for line in connections:
        key, values = line.split(": ")
        values = values.split(" ")
        values = [v for v in values if len(v) == 3]
        if key not in graph:
            graph[key] = values
        else:
            graph[key] += values
        if not simple:
            for value in values:
                if value not in graph:
                    graph[value] = [key]
                else:
                    graph[value] += [key]
    return graph


def compute_all_edges():
    edges = []
    simple_graph = create_graph_from_connections(data, simple=True)
    for key, values in simple_graph.items():
        for val in values:
            edges.append((key, val))
    return edges


def loop_over_graph(item: str, graph: dict, group: list):
    if item not in group:
        group += [item]

        conns = graph[item]
        for conn in conns:
            loop_over_graph(conn, graph, group)
    return group


def compute_groups(graph: dict):
    all_wires = list(graph)
    groups = []
    wires_left = all_wires.copy()
    while len(wires_left) > 0:
        wire = wires_left[-1]

        group = loop_over_graph(wire, graph, [])

        groups.append(group)
        wires_left = [i for i in wires_left if i not in group]
    return groups


def compute_data_without(d, edges):
    for edge in edges:
        k, v = edge
        for i, line in enumerate(d):
            if line.split(": ")[0] == k:
                d[i] = line.replace(v, "")
    return d


def get_path(start, end, graph):
    """
    returns the shortest path between start and end
    The solution doesn't NEED the shortest path (in fact it might be better random) but each cycle is quicker if we do
    """
    prev = {start: start}
    nodes = [start]
    seen = {start}
    while nodes:
        new_nodes = []
        for node in nodes:
            for neighbour in graph[node]:
                if neighbour in seen:
                    continue
                seen.add(neighbour)
                prev[neighbour] = node
                new_nodes.append(neighbour)
        nodes = new_nodes

    if prev.get(end) is None:
        return None

    path = []
    node = end
    while node != start:
        path.append(node)
        node = prev[node]
    path.append(start)
    return path[::-1]


# pak 10 random nodes
graph = create_graph_from_connections(data)
nodes = list(graph)
node_nrs = np.random.randint(0, len(nodes), 100)
random_nodes = [nodes[i] for i in node_nrs]

# bereken paden door graaf
alle_paden = {}
for i in it.combinations(random_nodes, 2):
    path = get_path(i[0], i[1], graph)
    for i in range(len(path) - 1):
        edge = tuple(sorted([path[i], path[i + 1]]))
        alle_paden[edge] = alle_paden.get(edge, 0) + 1

s_uses = sorted(alle_paden.items(), key=lambda x: x[1], reverse=True)
edges = [p[0] for p in s_uses[:3]]
e1 = (edges[0][1], edges[0][0])
e2 = (edges[1][1], edges[1][0])
e3 = (edges[2][1], edges[2][0])
edges += [e1, e2, e3]

# compute graph without 3 edges
data_copy = data.copy()
data_wo_edges = compute_data_without(data_copy, edges)
graph = create_graph_from_connections(data_wo_edges)
groups = compute_groups(graph)
if len(groups) == 2:
    print(len(groups[0]) * len(groups[1]))


edges = compute_all_edges()
for i in it.combinations(edges, 3):
    data_copy = data.copy()
    data_wo_edges = compute_data_without(data_copy, i)
    graph = create_graph_from_connections(data_wo_edges)
    groups = compute_groups(graph)
    if len(groups) == 2:
        print(i)
        print(len(groups[0]) * len(groups[1]))
