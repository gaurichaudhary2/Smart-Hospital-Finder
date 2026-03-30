import heapq

def ucs(graph, start, hospitals, allowed_types=None):
    pq = [(0, start, [start])]  # (cost, node, path)
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in hospitals:
            if not allowed_types or hospitals[node]["type"] in allowed_types:
                total_cost = cost + hospitals[node]["cost"]
                return node, total_cost, path

        if node in visited:
            continue

        visited.add(node)

        for neighbor, distance in graph[node].items():
            heapq.heappush(pq, (cost + distance, neighbor, path + [neighbor]))

    return None, None, []