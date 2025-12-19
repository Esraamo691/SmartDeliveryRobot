import heapq

#h(n)
def heuristic(current, goal):
    """Manhattan distance"""
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def astar(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    open_list = []
    heapq.heappush(open_list, (0, start))

# g(n)    
    g_cost = {start: 0}
    # To reconstruct the final path
    came_from = {}
    nodes_explored = 0

# Get the node with the lowest f = g + h
    while open_list:
        current_f, current = heapq.heappop(open_list)
        nodes_explored += 1

        if current == goal:
            break

        row, col = current
        # Possible movements: up, down, left, right
        neighbors = [
            (row + 1, col),
            (row - 1, col),
            (row, col + 1),
            (row, col - 1)
        ]

        for nr, nc in neighbors:
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == 'X':
                    continue
# g(n) of neighbor
                new_g = g_cost[current] + grid[nr][nc]

                if (nr, nc) not in g_cost or new_g < g_cost[(nr, nc)]:
                    g_cost[(nr, nc)] = new_g
                    f = new_g + heuristic((nr, nc), goal)
                    heapq.heappush(open_list, (f, (nr, nc)))
                    came_from[(nr, nc)] = current
                    
# Path Reconstruction 
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    return path, g_cost[goal], nodes_explored