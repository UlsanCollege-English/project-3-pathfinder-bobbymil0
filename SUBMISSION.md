# Project 3 Submission Summary

## What is included

- `src/project.py`: complete implementation of the required graph utilities.
- `data/map.json`: undirected weighted graph representing a festival campus map.
- `assets/map.png`: visual map image showing nodes, edges, and edge weights.
- `tests/test_project.py`: project tests plus additional edge-case coverage.
- `README.md`: completed project documentation with theme, usage, complexity, and limitations.
- `pytest.ini`: test configuration for reliable imports from the repository root.

## Features implemented

- `load_graph(path: str)` with validation for JSON format and positive integer weights.
- `get_neighbors(graph, node)` returning neighbor dictionaries or `{}` when missing.
- `bfs_order(graph, start)` using a queue, visited set, and dictionary order traversal.
- `dijkstra_distances(graph, start)` using `heapq` for shortest reachable distances.
- `shortest_path(graph, start, target)` with Dijkstra-based path reconstruction.
- `demo()` prints the loaded graph size, BFS order, distances, and a sample shortest path.

## Testing

- All tests pass: `pytest -q` → `20 passed`
- Additional edge cases covered:
  - invalid JSON top-level structure
  - invalid neighbor dictionary type
  - zero and negative weights
  - BFS neighbor-order traversal

## Notes

- The graph is undirected; each edge appears in both directions in `data/map.json`.
- Weights are positive integers representing walking cost.
- The project is ready for submission.
