[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/RNukvtFO)
# Project 3: Pathfinder

## Map Theme

This project models a small campus festival pathfinder that helps visitors move between festival locations on an undirected weighted map. The map is based on a festival layout with six key locations and walking distances between them.

## Map Picture

![Project map](assets/map.png)

The map shows:
- six festival locations as nodes,
- the undirected paths between those locations,
- the cost of each path as a positive integer representing walking time.

## How the Graph Works

### Nodes

Each node represents a festival location in the campus event area:
- `Gate`
- `Food Court`
- `Main Stage`
- `Rest Area`
- `First Aid`
- `Game Booth`

### Edges

Each edge represents a bidirectional walking path between two festival locations.

### Weights

Each weight is a positive integer representing the walking cost between two locations. In this project the weight is treated as a walking distance or time cost.

## Features Implemented

Check the features you completed:

- [x] Load graph from JSON
- [x] Get neighbors
- [x] BFS traversal
- [x] Dijkstra shortest distances
- [x] Shortest path reconstruction
- [x] Demo function
- [x] Extra tests
- [ ] Stretch feature: Not implemented

## How to Run

Run the demo from the command line:

```bash
python src/project.py
```

The demo loads `data/map.json`, prints the number of locations, shows BFS order from the first location, prints shortest distances from that location, and prints one shortest path.

## How to Test

Run the test suite with pytest from the project root:

```bash
PYTHONPATH=. pytest -q
```

If your environment has pytest installed for the local Python interpreter, you can also use:

```bash
python3 -m pytest -q
```

## Complexity

### BFS

Time:

```text
O(V + E)
```

Space:

```text
O(V)
```

Explanation:
Breadth-first search visits each node once and examines each edge at most once, storing visited nodes and a queue of nodes to explore.

### Dijkstra

Time:

```text
O((V + E) log V)
```

Space:

```text
O(V)
```

Explanation:
Dijkstra uses a priority queue to select the next node with the shortest tentative distance. Each node is pushed to the heap at most once for each improvement, and distance data is stored for reachable nodes.

### Shortest Path Reconstruction

Time:

```text
O(P)
```

Space:

```text
O(P)
```

Explanation:
After Dijkstra computes shortest distances, the algorithm steps backward from the target to the start using parent pointers. This reconstruction is linear in the number of nodes in the returned path.

## Edge Cases

Check the edge cases your project handles:

- [x] Empty graph
- [x] Missing start node
- [x] Missing target node
- [x] Start equals target
- [x] Unreachable target
- [x] Graph with a cycle
- [ ] Graph with one node
- [x] Disconnected graph
- [x] Multiple possible paths
- [x] Zero weight rejected
- [x] Negative weight rejected

Add notes about edge cases here:

This project validates graph structure, rejects non-dictionary graph formats, rejects non-integer or non-positive weights, and handles missing nodes gracefully.

## Known Limitations

- The implementation only supports undirected weighted graphs.
- The project does not support negative or zero weights.
- The demo is command-line only and does not include a graphical user interface.
- If there are multiple equal-cost shortest paths, the algorithm returns one valid shortest path.

## Assistance & Sources

### AI Used?

Yes

### What AI Helped With

AI helped with implementing the graph utilities, validating edge-case behavior, and improving the README wording.

### Other Sources

No outside sources used.
