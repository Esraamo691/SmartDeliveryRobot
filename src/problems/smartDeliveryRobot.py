# 1  = normal road
# 3  = high traffic road
# X  = blocked road

grid = [
    [1, 1, 1, 1, 1, 1],
    [1, 'X', 'X', 'X', 3, 1],
    [1, 3, 3, 'X', 3, 1],
    [1, 1, 1, 'X', 1, 1],
    ['X', 'X', 1, 1, 1, 'X'],
    [1, 1, 1, 'X', 1, 1]
]

start = (5, 0)
goal  = (0, 5)