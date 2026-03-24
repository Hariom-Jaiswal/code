def is_safe(board, row, col, n):
    # Check left side (row)
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col, n):
    # All queens placed
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve_nqueens(board, col + 1, n):
                return True

            # Backtrack
            board[i][col] = 0

    return False


def print_board(board):
    for row in board:
        print(row)


# N value
n = 4

# Initialize board
board = [[0 for _ in range(n)] for _ in range(n)]

if solve_nqueens(board, 0, n):
    print("Solution:")
    print_board(board)
else:
    print("No solution exists")