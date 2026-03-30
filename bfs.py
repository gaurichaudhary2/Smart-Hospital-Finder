from collections import deque

def bfs(graph, start, hospitals, allowed_types=None):
    visited = set()
    queue = deque([(start, [start])])  # (node, path)

    while queue:
        node, path = queue.popleft()

        if node in hospitals:
            if not allowed_types or hospitals[node]["type"] in allowed_types:
                return node, path

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None, []