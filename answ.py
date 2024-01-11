from collections import defaultdict

in_degree = [0] * (warehouse_nodes + 1)

def dfs(node, graph, used_edges, in_degree):
    for neighbor in graph[node]:
        edge = (node, neighbor)
        print(edge)
        if edge not in used_edges:
            used_edges.add(edge)
            in_degree[neighbor] += 1
            dfs(neighbor, graph, used_edges, in_degree)

def min_weakly_connected_nodes(warehouse_nodes, warehouse_edges, warehouse_from, warehouse_to):
    graph = defaultdict(list)
    used_edges = set()



    # Create the directed graph
    for i in range(warehouse_edges):
        graph[warehouse_from[i]].append(warehouse_to[i])

    for i in range(1, warehouse_edges):
        # Perform DFS to mark edges used and calculate in-degrees
        dfs(i, graph, used_edges, in_degree)

    print(in_degree)

    # Count the number of weakly connected nodes (nodes with 0 indegree)
    weakly_connected = sum(1 for degree in in_degree if degree == 0) - 1  # Excluding the starting node

    return weakly_connected

# Given input
warehouse_nodes = 6
warehouse_edges = 5
warehouse_from = [1, 2, 4, 5, 4]
warehouse_to = [2, 3, 5, 6, 6]

result = min_weakly_connected_nodes(warehouse_nodes, warehouse_edges, warehouse_from, warehouse_to)
print("Minimum number of weakly connected nodes:", result)
