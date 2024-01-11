from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_iterative(self, start_node):
        visited = set()
        stack = [(start_node, 0)]  # Stack to keep track of nodes and their depths
        max_depth = {node: 0 for node in self.graph}  # Dictionary to store max depth for each node

        while stack:
            node, depth = stack.pop()
            if node not in visited:
                visited.add(node)
                # Update max depth for the current node if necessary
                max_depth[node] = max(max_depth[node], depth)

                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        stack.append((neighbor, depth + 1))

        return max_depth

# Example usage:
edges_from = [1, 2, 3, 3, 1, 1]
edges_to = [2, 3, 4, 5, 6, 7]



g = Graph()

# Adding edges to the graph
for i in range(len(edges_from)):
    g.add_edge(edges_from[i], edges_to[i])

start_node = 1  # Change this to your desired starting node
print("DFS traversal from node", start_node)
max_depths = g.dfs_iterative(start_node)

print("Maximum depths reached from each node:")
for node, depth in max_depths.items():
    print(f"Node {node}: {depth}")