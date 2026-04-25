import os
import heapq
import networkx as nx
import matplotlib.pyplot as plt

os.makedirs("outputs", exist_ok=True)

edges = [
    ("A", "B", 2),
    ("A", "C", 6),
    ("B", "C", 1),
    ("B", "D", 5),
    ("C", "D", 2),
    ("C", "E", 4),
    ("D", "E", 1),
    ("D", "F", 3),
    ("E", "F", 2),
]

def build_graph(edge_list):
    graph = {}
    for u, v, w in edge_list:
        graph.setdefault(u, {})[v] = w
        graph.setdefault(v, {})[u] = w
    return graph

def dijkstra(graph, source):
    dist = {node: float("inf") for node in graph}
    prev = {node: None for node in graph}
    dist[source] = 0

    pq = [(0, source)]
    visited = set()
    trace = []

    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue

        visited.add(u)
        trace.append((u, d, dict(dist)))

        for v, w in graph[u].items():
            if d + w < dist[v]:
                dist[v] = d + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, prev, trace

def path_to(prev, source, dest):
    path = []
    node = dest
    while node is not None:
        path.append(node)
        node = prev[node]
    path.reverse()
    return path if path and path[0] == source else []

def forwarding_table(prev, source):
    table = {}
    for dest in prev:
        if dest == source:
            continue
        path = path_to(prev, source, dest)
        table[dest] = path[1] if len(path) > 1 else None
    return table

def print_table(title, graph, source="A"):
    dist, prev, trace = dijkstra(graph, source)
    print("\n" + title)
    print("Destination | Cost | Path")
    for dest in sorted(graph):
        p = path_to(prev, source, dest)
        print(f"{dest:>11} | {dist[dest]:>4} | {' -> '.join(p)}")

    print("Forwarding table from A:", forwarding_table(prev, source))
    return dist, prev

def draw_graph(edge_list, filename, title):
    G = nx.Graph()
    for u, v, w in edge_list:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G, seed=7)
    labels = nx.get_edge_attributes(G, "weight")

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=1200, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(f"outputs/{filename}", dpi=200)
    plt.show()

graph = build_graph(edges)
initial_dist, initial_prev = print_table("Initial shortest paths", graph)

failed_edges = [edge for edge in edges if set(edge[:2]) != set(("C", "D"))]
failed_graph = build_graph(failed_edges)
failed_dist, failed_prev = print_table("After C-D link failure", failed_graph)

affected = [
    node for node in initial_dist
    if initial_dist[node] != failed_dist[node]
]
print("Affected destinations after C-D failure:", affected)

draw_graph(edges, "routing_graph_initial.png", "Initial Network Graph")
draw_graph(failed_edges, "routing_graph_after_failure.png", "Network Graph After C-D Failure")
