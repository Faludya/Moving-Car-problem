# 🚗 Moving Vehicles — A* Search on an m×m Parking Grid

This project models a search problem where **m vehicles** start on the bottom row of an **m×m** grid and must reach the **top row in reverse order** (vehicle `i` from `(i,1)` → `(m−i+1, m)`).  
Vehicles move one cell per step (U/D/L/R) or **stay**; additionally, **one adjacent vehicle may jump over a stationary neighbor** in a single step. **No two vehicles may share a cell.** :contentReference[oaicite:0]{index=0}

---

## 🧩 Problem Definition

- **State**: positions of all `m` vehicles on the grid.  
- **Actions per vehicle**: `Stay`, `MoveUp/Down/Left/Right`, `JumpUp/Down/Left/Right` (subject to bounds, occupancy, and jump rules). :contentReference[oaicite:1]{index=1}  
- **Goal**: top row in reversed order (permutation mirror). :contentReference[oaicite:2]{index=2}
- **Constraints**: single-cell moves or a single jump over one adjacent vehicle; no collisions. :contentReference[oaicite:3]{index=3}

---

## 🎯 Approach

- **Heuristic**: Manhattan-distance–based bound per car; ideal-case analysis yields lower/upper limits. The project uses  
  \[
  h = \sum | \text{currentState} - \text{goalState} | \times 2
  \]
  which proved effective for guiding search. :contentReference[oaicite:4]{index=4}
- **Algorithms compared**: BFS, DFS, Best-First, and **A\*** (with `f(n)=g(n)+h(n)`). Empirically, **A\*** offered the best balance of path quality and runtime across layouts, while BFS often found optimal paths but was slow, and DFS/Best-First were inconsistent/non-optimal in some settings. :contentReference[oaicite:5]{index=5}

---

## 📊 Highlights from Experiments

Two layout families were tested (bottom→top vs. left→right arrangements) and multiple grid sizes.  
Examples (abridged):

- **Layout 1 (bottom to top)**  
  - `m=4`: BFS optimal but slow; Best-First non-optimal but faster; DFS/A* had failure cases depending on layout configuration. :contentReference[oaicite:6]{index=6}

- **Layout 2 (row-to-row)**  
  - `m=4`: A* produced competitive paths with tractable runtime, making it the preferred final choice for more results. :contentReference[oaicite:7]{index=7}

- **A*** scaling snapshot (final runs):  
  `m=2 → cost 6`, `m=3 → cost 11`, `m=4 → cost 19`, `m=7 → cost 134` (runtime grows quickly as state space explodes). :contentReference[oaicite:8]{index=8}

Graphs of **path cost**, **considered actions**, and **runtime** vs. `m` illustrate rapid growth and motivate the A* selection. :contentReference[oaicite:9]{index=9}

---

## 🗂 Project Structure

Project/
├─ main.py # Orchestrates I/O, timing, and runs the solver

├─ movingVehicles.py # Problem class: states, actions, result, heuristic

├─ search.py # Generic Problem/Node + BFS/DFS/Best-First/A* utilities

├─ utils.py # Helpers (I/O, formatting, etc.)

├─ InputData/ # Test inputs (size m)

├─ OutputData/ # Solver outputs and logs

└─ Documentation.pdf # Report with results and figures

### Output
Output (written to OutputData/ and partially shown in console):

Sequence of grid states (console pretty-print)

Sequence of actions

Total path cost, #considered action lists, and runtime (for comparison across algorithms/sizes). 

Note: full matrix sequences are printed via a custom __repr__; file logging focuses on summaries/metrics.
<img width="1794" height="570" alt="exemplu" src="https://github.com/user-attachments/assets/f1d519b5-d5c8-44ee-acc3-15903cdc3479" />
