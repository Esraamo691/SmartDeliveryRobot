import sys
sys.dont_write_bytecode=True
from problems.smartDeliveryRobot import grid, start, goal
from algorithms.ucs import ucs
from algorithms.astar import astar
from algorithms.bfs import bfs
import time
import csv
import os

os.makedirs("results/performance", exist_ok=True)

# UCS
start_time = time.time()
ucs_path, ucs_cost, ucs_nodes = ucs(grid, start, goal)
end_time = time.time()
ucs_time = (end_time - start_time)*1000

print("UCS Path:")
for step in ucs_path:
    print(step)

print("\n"+"="*50+"\n")
# A*
start_time = time.time()
astar_path, astar_cost, astar_nodes = astar(grid, start, goal)
end_time = time.time()
astar_time = (end_time - start_time)*1000

print("A* Path:")
for step in astar_path:
    print(step)

print("\n"+"="*50+"\n")

#BFS
start_time = time.time()
bfs_path, bfs_cost, bfs_nodes = bfs(grid, start, goal)
end_time = time.time()
bfs_time = (end_time - start_time)*1000

print("BFS Path:")
for step in bfs_path:
    print(step)


print("UCS Cost:", ucs_cost, "Nodes:", ucs_nodes)
print("A* Cost:", astar_cost, "Nodes:", astar_nodes)
print("BFS Cost:", bfs_cost, "Nodes:", bfs_nodes)

# Save CSV
with open("results/performance/comparison.csv","w",newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Algorithm","Path Cost","Nodes Explored","Time (ms)"])
    writer.writerow(["UCS", ucs_cost, ucs_nodes, round(ucs_time,2)])
    writer.writerow(["A*", astar_cost, astar_nodes, round(astar_time,2)])
    writer.writerow(["BFS", bfs_cost, bfs_nodes, round(bfs_time,2)])


