"""Project 3: Pathfinder.

Implement graph utilities for an undirected weighted map.

Rules:
- Python 3.11+
- stdlib only
- weights must be positive integers (no zero or negative weights)
- graph representation: dict[str, dict[str, int]]

Example graph:

    {
        "Gate": {
            "Food Court": 4,
            "Stage": 7,
        },
        "Food Court": {
            "Gate": 4,
            "Rest Area": 3,
        },
    }

Students:
- Replace each NotImplementedError with your implementation.
- Keep function names and parameters exactly as written.
- Add helper functions if they make your code clearer.
"""

from __future__ import annotations

from collections import deque
import heapq
import json
import math
from pathlib import Path


Graph = dict[str, dict[str, int]]


def _validate_graph(graph: Graph) -> None:
    for node, neighbors in graph.items():
        if not isinstance(node, str):
            raise ValueError("Graph nodes must be strings")
        if not isinstance(neighbors, dict):
            raise ValueError("Each node must map to a dictionary of neighbors")
        for neighbor, weight in neighbors.items():
            if not isinstance(neighbor, str):
                raise ValueError("Neighbor names must be strings")
            if not isinstance(weight, int):
                raise ValueError("Edge weights must be integers")
            if weight <= 0:
                raise ValueError("Edge weights must be positive integers")


def load_graph(path: str) -> Graph:
    """Load a weighted graph from a JSON file.

    The JSON file must contain a dictionary of dictionaries:

        {
            "A": {"B": 3, "C": 5},
            "B": {"A": 3},
            "C": {"A": 5}
        }

    Requirements:
    - Return the loaded graph.
    - Raise ValueError if the JSON top level is not a dictionary.
    - Raise ValueError if any neighbor list is not a dictionary.
    - Raise ValueError if any weight is not a positive integer.
    - Raise ValueError if any weight is 0 or negative.

    Note:
    This project uses an undirected graph. Your own map should include both
    directions for every edge, such as A -> B and B -> A.
    """
    map_path = Path(path)
    raw_data = json.loads(map_path.read_text(encoding="utf-8"))
    if not isinstance(raw_data, dict):
        raise ValueError("Graph JSON must contain a dictionary at the top level")
    graph: Graph = {}
    for node, neighbors in raw_data.items():
        if not isinstance(neighbors, dict):
            raise ValueError("Each node must map to a dictionary of neighbors")
        graph[node] = {}
        for neighbor, weight in neighbors.items():
            if not isinstance(weight, int):
                raise ValueError("Edge weights must be integers")
            if weight <= 0:
                raise ValueError("Edge weights must be positive integers")
            graph[node][neighbor] = weight
    _validate_graph(graph)
    return graph


def get_neighbors(graph: Graph, node: str) -> dict[str, int]:
    """Return the neighbors and weights for node.

    If node is missing, return an empty dictionary.

    Example:
        graph = {"A": {"B": 4}}
        get_neighbors(graph, "A") -> {"B": 4}
        get_neighbors(graph, "Z") -> {}
    """
    return graph.get(node, {})


def bfs_order(graph: Graph, start: str) -> list[str]:
    """Return nodes in breadth-first traversal order.

    Requirements:
    - If start is missing, return [].
    - Use a queue.
    - Use a visited set.
    - Follow the neighbor order from the dictionary.
    - Ignore weights for BFS traversal.

    Complexity target:
    - Time: O(V + E)
    - Space: O(V)
    """
    if start not in graph:
        return []
    visited: set[str] = {start}
    order: list[str] = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, {}):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def dijkstra_distances(graph: Graph, start: str) -> dict[str, float]:
    """Return shortest distances from start to every reachable node.

    Requirements:
    - Use Dijkstra's algorithm.
    - Use heapq as the priority queue.
    - If start is missing, return {}.
    - Ignore unreachable nodes; they should not appear in the result.
    - All edge weights must be positive integers.
    - Raise ValueError if a zero or negative weight is found.

    Example:
        graph = {
            "A": {"B": 4, "C": 2},
            "B": {"A": 4},
            "C": {"A": 2}
        }

        dijkstra_distances(graph, "A") -> {"A": 0, "B": 4, "C": 2}

    Complexity target:
    - Time: O((V + E) log V)
    - Space: O(V)
    """
    if start not in graph:
        return {}
    _validate_graph(graph)
    distances: dict[str, float] = {start: 0.0}
    heap: list[tuple[float, str]] = [(0.0, start)]
    while heap:
        current_distance, node = heapq.heappop(heap)
        if current_distance > distances[node]:
            continue
        for neighbor, weight in graph.get(node, {}).items():
            distance = current_distance + float(weight)
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return distances


def shortest_path(graph: Graph, start: str, target: str) -> list[str]:
    """Return the shortest path from start to target.

    Requirements:
    - Use Dijkstra's algorithm with path reconstruction.
    - Return a list of node names in path order.
    - If start or target is missing, return [].
    - If target is unreachable from start, return [].
    - If start == target and start exists, return [start].
    - Raise ValueError if a zero or negative weight is found.

    Example:
        shortest_path(graph, "A", "D") -> ["A", "C", "D"]

    Complexity target:
    - Dijkstra portion: O((V + E) log V)
    - Path reconstruction: O(P), where P is the number of nodes in the path
    """
    if start not in graph or target not in graph:
        return []
    if start == target:
        return [start]
    _validate_graph(graph)
    distances: dict[str, float] = {start: 0.0}
    parents: dict[str, str] = {}
    heap: list[tuple[float, str]] = [(0.0, start)]
    while heap:
        current_distance, node = heapq.heappop(heap)
        if current_distance > distances[node]:
            continue
        if node == target:
            break
        for neighbor, weight in graph.get(node, {}).items():
            distance = current_distance + float(weight)
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = node
                heapq.heappush(heap, (distance, neighbor))
    if target not in distances:
        return []
    path: list[str] = []
    current = target
    while current != start:
        path.append(current)
        current = parents.get(current)
        if current is None:
            return []
    path.append(start)
    path.reverse()
    return path


def demo() -> None:
    """Print a short demonstration of your project.

    Your demo should:
    1. Load your graph from data/map.json.
    2. Print the number of locations.
    3. Print BFS order from one location.
    4. Print shortest distances from one location.
    5. Print one shortest path.

    This function is not directly graded by the public tests, but it is useful
    for your presentation/demo.
    """
    map_file = Path(__file__).resolve().parent.parent / "data" / "map.json"
    graph = load_graph(str(map_file))

    if not graph:
        print("Graph is empty or could not be loaded.")
        return
    start = next(iter(graph))
    target = None
    for node in graph:
        if node != start:
            target = node
            break

    print(f"Loaded graph with {len(graph)} locations.")
    print(f"BFS order from {start}: {bfs_order(graph, start)}")
    print(f"Shortest distances from {start}:")
    distances = dijkstra_distances(graph, start)
    for node, distance in sorted(distances.items()):
        print(f"  {node}: {distance}")
    if target is not None:
        print(f"Shortest path from {start} to {target}: {shortest_path(graph, start, target)}")


if __name__ == "__main__":
    demo()
