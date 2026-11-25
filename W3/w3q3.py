from collections import deque

grid = [
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 0]
]
def robot_path(grid):
    rows = len(grid)
    cols = len(grid[0])

    start = (0, 0)
    end = (rows - 1, cols - 1)

    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return None

    queue = deque([(0, 0, [(0, 0)])])
    visited = {(0, 0)}

    # Right and Down only
    directions = [(0, 1), (1, 0)]

    while queue:
        r, c, path = queue.popleft()

        if (r, c) == end:
            return path
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if (0 <= nr < rows and
                0 <= nc < cols and
                grid[nr][nc] == 0 and
                (nr, nc) not in visited):

                visited.add((nr, nc))
                queue.append((nr, nc, path + [(nr, nc)]))
    return None


path = robot_path(grid)

if path:
    print("Robot Path:", path)
else:
    print("No path exists.")
