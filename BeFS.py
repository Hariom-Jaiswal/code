from queue import PriorityQueue

# Graph with costs (not used here, just structure)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Heuristic values (lower = closer to goal)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 2,
    'F': 0   # Goal node
}

def best_first_search(start, goal):
    visited = set()
    pq = PriorityQueue()

    # (heuristic, node)
    pq.put((heuristic[start], start))

    print("Traversal:")

    while not pq.empty():
        h, node = pq.get()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            if node == goal:
                print("\nGoal reached!")
                return

            for neighbor in graph[node]:
                if neighbor not in visited:
                    pq.put((heuristic[neighbor], neighbor))

    print("\nGoal not found")


# Run
best_first_search('A', 'F')