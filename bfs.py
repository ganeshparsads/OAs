from collections import defaultdict, deque

def min_unreachable_warehouses(warehouse_nodes, warehouse_edges, warehouse_from, warehouse_to):
    graph = defaultdict(list)
    in_degree = [0] * (warehouse_nodes + 1)

    # Create the directed graph and calculate in-degrees
    for i in range(warehouse_edges):
        graph[warehouse_from[i]].append(warehouse_to[i])
        in_degree[warehouse_to[i]] += 1

    # Perform BFS to count unreachable warehouses
    queue = deque()
    unreachable_count = 0

    # Initialize the queue with warehouses having in-degree 0
    for i in range(1, warehouse_nodes + 1):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Count the number of unreachable warehouses
    for i in range(1, warehouse_nodes + 1):
        if in_degree[i] == 0:
            unreachable_count += 1

    return unreachable_count

# Example input
warehouse_nodes = 6
warehouse_edges = 5
warehouse_from = [1, 2, 4, 5, 4]
warehouse_to = [2, 3, 5, 6, 6]

result = min_unreachable_warehouses(warehouse_nodes, warehouse_edges, warehouse_from, warehouse_to)
print("Minimum number of unreachable warehouses:", result)
