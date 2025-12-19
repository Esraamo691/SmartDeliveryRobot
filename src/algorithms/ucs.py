import heapq

def ucs(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    pq = []
    heapq.heappush(pq, (0, start, [start]))

    visited = {}
    nodes_explored = 0

    while pq:
        cost, current, path = heapq.heappop(pq)
        nodes_explored += 1

        if current == goal:
            return path, cost, nodes_explored

        if current in visited and visited[current] <= cost:
            continue

        visited[current] = cost

        x, y = current
        moves = [(-1,0), (1,0), (0,-1), (0,1)]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] != 'X':
                    new_cost = cost + grid[nx][ny]
                    heapq.heappush(
                        pq,
                        (new_cost, (nx, ny), path + [(nx, ny)])
                    )

    return None, None, nodes_explored