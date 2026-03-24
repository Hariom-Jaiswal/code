class Graph:
    def __init__(self):
        self.graph = {}

    # Add edge
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)

    # DFS using stack
    def dfs(self, start):
        visited = set()
        stack = [start]

        print("DFS Traversal:")

        while stack:
            node = stack.pop()

            if node not in visited:
                print(node, end=" ")
                visited.add(node)

                # Add neighbors in reverse order
                for neighbor in reversed(self.graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)


# Create graph
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('E', 'F')

# Run DFS
g.dfs('A')