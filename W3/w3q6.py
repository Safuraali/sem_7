N = 8

moves = [
    (2, 1), (2, -1),
    (-2, 1), (-2, -1),
    (1, 2), (1, -2),
    (-1, 2), (-1, -2)
]


def is_valid(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1


def count_onward_moves(x, y, board):
    count = 0

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if is_valid(nx, ny, board):
            count += 1

    return count


def knight_tour(board, x, y, move_number):
    if move_number == N * N:
        return True

    candidates = []

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if is_valid(nx, ny, board):
            degree = count_onward_moves(nx, ny, board)
            candidates.append((degree, nx, ny))

    # Visit the square with the fewest onward moves first.
    candidates.sort()

    for _, nx, ny in candidates:
        board[nx][ny] = move_number

        if knight_tour(board, nx, ny, move_number + 1):
            return True

        # Backtrack
        board[nx][ny] = -1

    return False

board = [[-1 for _ in range(N)] for _ in range(N)]

#top-left 
board[0][0] = 0

if knight_tour(board, 0, 0, 1):
    print("Knight's Tour:")
    for row in board:
        print(row)
else:
    print("No solution found.")
