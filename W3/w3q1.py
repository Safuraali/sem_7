from collections import deque
def bfs_maze(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    queue = deque([(start, [start])])
    visited = {start}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == end:
            return path
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and
                0 <= nc < cols and
                maze[nr][nc] == 0 and
                (nr, nc) not in visited):
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
    return None
maze = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 1, 0],
    [0, 0, 0, 0]
]
start = (0, 0)
end = (3, 3)
path = bfs_maze(maze, start, end)
if path:
    print("Shortest Path:", path)
else:
    print("No path exists.")



