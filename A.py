from queue import PriorityQueue

# Graph with costs
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 5},
    'D': {},
    'E': {'F': 2},
    'F': {}
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 2,
    'F': 0
}

def a_star(start, goal):
    pq = PriorityQueue()
    pq.put((0, start))

    g_cost = {start: 0}
    parent = {start: None}

    while not pq.empty():
        f, node = pq.get()

        if node == goal:
            break

        for neighbor in graph[node]:
            cost = g_cost[node] + graph[node][neighbor]

            if neighbor not in g_cost or cost < g_cost[neighbor]:
                g_cost[neighbor] = cost
                f_cost = cost + heuristic[neighbor]
                pq.put((f_cost, neighbor))
                parent[neighbor] = node

    # Reconstruct path
    path = []
    current = goal
    while current:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("Shortest Path:", path)
    print("Cost:", g_cost[goal])


# Run
a_star('A', 'F')