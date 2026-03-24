import copy

# Goal state
goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

# Heuristic: count misplaced tiles
def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

# Find blank position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate neighbors
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    moves = [(-1,0),(1,0),(0,-1),(0,1)]  # up, down, left, right

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

# Hill Climbing
def hill_climbing(start):
    current = start

    while True:
        current_h = heuristic(current)
        neighbors = get_neighbors(current)

        # Find best neighbor
        best = current
        best_h = current_h

        for n in neighbors:
            h = heuristic(n)
            if h < best_h:
                best = n
                best_h = h

        # If no better neighbor → stop
        if best_h >= current_h:
            break

        current = best

    return current

# Print state
def print_state(state):
    for row in state:
        print(row)
    print()

# Initial state
start = [[1,2,3],
         [4,0,6],
         [7,5,8]]

result = hill_climbing(start)

print("Final State:")
print_state(result)
print("Heuristic:", heuristic(result))