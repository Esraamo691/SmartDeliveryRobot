#  Smart Delivery Robot Path Planning

##  Project Overview
This project addresses the *Smart Delivery Robot Path Planning* problem using classical AI search algorithms.  
The objective is to find the *most cost-efficient path* for a delivery robot moving from a warehouse to a customer inside a city-like grid environment.

Unlike traditional shortest-path problems, different roads have different costs, making the problem more realistic and suitable for AI search techniques.

---

##  Problem Description
The environment is modeled as a *2D grid*, where each cell represents a road type:

- 🟩 *Free Road* (normal cost)
- 🟥 *Blocked Road* (obstacle)
- 🟨 *High-Traffic Road* (higher cost)

The robot can move:
- ⬆ Up  
- ⬇ Down  
- ⬅ Left  
- ➡ Right  

Each movement has a cost depending on the road type.

---

##  Goal
Find the *optimal path* that minimizes the *total delivery cost* (time or effort), not just the number of steps.

---

## 💡 Why This Problem?
- Realistic delivery & robotics scenario
- Clearly defined state space
- Supports multiple search algorithms
- Highlights the importance of heuristics
- Demonstrates trade-offs between:
  - Optimality
  - Time
  - Memory usage

---

##  Implementation Details

### 🔹 State Representation
Each state is represented as:(x,y)
Where x is the row and y is the column in the grid.
Example:(3,2)

---

### 🔹 Successor Function
From any position, the robot can move to adjacent cells if:
- The cell is inside the grid
- The cell is not blocked

---

### 🔹 Cost Function
| Road Type | Cost |
|----------|------|
| Normal Road | 1 |
| High-Traffic Road | 3 |
| Blocked Road | Not Allowed |

The total path cost is the sum of all movement costs.

---

### 🔹 Heuristic Function (A*)
- *Manhattan Distance*
- Admissible heuristic
- Reduces explored nodes significantly

---

## 🧠 Algorithms Implemented
- *BFS (Breadth-First Search)*  
  Finds the shortest path in steps (ignores cost)

- *UCS (Uniform Cost Search)*  
  Guarantees the lowest-cost path

- *A\**  
  Uses heuristics to find the optimal path efficiently

---

##  Expected Results

| Algorithm | Path Cost | Nodes Explored | Time |
|---------|-----------|---------------|------|
| BFS | High | Large | Medium |
| UCS | Optimal | Medium | Medium |
| A* | Optimal | Small | Low |

---

---

## 👥 Team Members & Roles

| Name | ID | Role |
|----|----|----|
| *Esraa Mohamed ElSaeed Matouq* | 2023037 | Project Manager, file organization, proposal & integration |
| *Aya Sherif Abou ElFotouh Shalaby* | 2023055 | A* Algorithm Implementation |
| *Esraa Islam Mohamed ElAshry* | 2023033 | Uniform Cost Search (UCS) Implementation |
| *Mariam Mohamed Hassan ElAshqar* | 2023209 | Breadth-First Search (BFS) Implementation |
| *Doaa Ehab Mohamed ElSabbagh* | 2023078 | Results analysis & visualization |

---

## 📈 Results & Visualization
The results/ directory includes:
- 📊 Performance comparison tables
- 📉 Bar charts (cost, time, explored nodes)
- 🗺 Grid-based path visualizations for each algorithm

---

## ✅ Conclusion
This project demonstrates how AI search algorithms can be applied to a realistic delivery robot scenario.  
The comparison clearly shows that *heuristic-based search (A\)** achieves optimal solutions with significantly better efficiency.

---
