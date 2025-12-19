# Smart Delivery Robot Path Planning

## Project Overview

This project addresses the _Smart Delivery Robot Path Planning_ problem using classical AI search algorithms.  
The objective is to find the _most cost-efficient path_ for a delivery robot moving from a warehouse to a customer inside a city-like grid environment.

Unlike traditional shortest-path problems, different roads have different costs, making the problem more realistic and suitable for AI search techniques.

---

## Problem Description

The environment is modeled as a _2D grid_, where each cell represents a road type:

- _Free Road_ (normal cost)
- _Blocked Road_ (obstacle)
- _High-Traffic Road_ (higher cost)

The robot can move:

- ⬆ Up
- ⬇ Down
- ⬅ Left
- ➡ Right

Each movement has a cost depending on the road type.

---

## Goal

Find the _optimal path_ that minimizes the _total delivery cost_ (time or effort), not just the number of steps.

---

## Why This Problem?

- Realistic delivery & robotics scenario
- Clearly defined state space
- Supports multiple search algorithms
- Highlights the importance of heuristics
- Demonstrates trade-offs between:
  - Optimality
  - Time
  - Memory usage

---

## Implementation Details

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

| Road Type         | Cost        |
| ----------------- | ----------- |
| Normal Road       | 1           |
| High-Traffic Road | 3           |
| Blocked Road      | Not Allowed |

The total path cost is the sum of all movement costs.

---

### 🔹 Heuristic Function (A\*)

- _Manhattan Distance_
- Admissible heuristic
- Reduces explored nodes significantly

---

## Algorithms Implemented

- _BFS (Breadth-First Search)_  
  Finds the shortest path in steps (ignores cost)

- _UCS (Uniform Cost Search)_  
  Guarantees the lowest-cost path

- \*A\*\*  
  Uses heuristics to find the optimal path efficiently

---

## Expected Results

| Algorithm | Path Cost | Nodes Explored | Time   |
| --------- | --------- | -------------- | ------ |
| BFS       | High      | Large          | Medium |
| UCS       | Optimal   | Medium         | Medium |
| A\*       | Optimal   | Small          | Low    |

---

---

## Team Members & Roles

| Name                               | ID      | Role                                                       |
| ---------------------------------- | ------- | ---------------------------------------------------------- |
| _Esraa Mohamed ElSaeed Matouq_     | 2023037 | Project Manager, file organization, proposal & integration |
| _Aya Sherif Abou ElFotouh Shalaby_ | 2023055 | A\* Algorithm Implementation                               |
| _Esraa Islam Mohamed ElAshry_      | 2023033 | Uniform Cost Search (UCS) Implementation                   |
| _Mariam Mohamed Hassan ElAshqar_   | 2023209 | Breadth-First Search (BFS) Implementation                  |
| _Doaa Ehab Mohamed ElSabbagh_      | 2023078 | Results analysis & visualization                           |

---

## Results & Visualization

The results/ directory includes:

- Performance comparison tables
- Bar charts (cost, time, explored nodes)
- Grid-based path visualizations for each algorithm

---

## Conclusion

This project demonstrates how AI search algorithms can be applied to a realistic delivery robot scenario.  
The comparison clearly shows that \*heuristic-based search (A\)\*\* achieves optimal solutions with significantly better efficiency.

---
