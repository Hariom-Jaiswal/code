from collections import deque

def water_jug_bfs(capA, capB, target):
    visited = set()
    queue = deque()

    # Initial state
    queue.append((0, 0))
    visited.add((0, 0))

    while queue:
        x, y = queue.popleft()
        print(f"State: ({x}, {y})")

        # Check goal
        if x == target or y == target:
            print("Target reached!")
            return

        # Possible operations
        next_states = [
            (capA, y),       # Fill A
            (x, capB),       # Fill B
            (0, y),          # Empty A
            (x, 0),          # Empty B
            # Pour A → B
            (x - min(x, capB - y), y + min(x, capB - y)),
            # Pour B → A
            (x + min(y, capA - x), y - min(y, capA - x))
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    print("No solution found")


# Run
water_jug_bfs(4, 3, 2)