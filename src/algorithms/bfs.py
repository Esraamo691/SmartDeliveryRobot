from collections import deque

def bfs(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    
    queue = deque()
    queue.append((start, [start], 0))  # position, path, cost
    visited = set()
    nodes_explored = 0
    
    while queue:
        current, path, cost = queue.popleft()
        nodes_explored += 1

        if current == goal:
            return path, cost, nodes_explored

        if current in visited:
            continue
        visited.add(current)

        row, col = current
        neighbors = [
            (row+1, col),
            (row-1, col),
            (row, col+1),
            (row, col-1)
        ]

        for nr, nc in neighbors:
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] != 'X' and (nr, nc) not in visited:
                    new_cost = cost + grid[nr][nc]
                    queue.append(((nr, nc), path + [(nr, nc)], new_cost))

    return None, None, nodes_explored