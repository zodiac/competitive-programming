def dijkstra(n, graph, start):
    """ Uses Dijkstra's algortihm to find the shortest path between in a graph. """
    from heapq import heappop, heappush

    dist = [float("inf")] * n
    dist[start] = 0

    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if path_len != dist[v]: continue

        for w, edge_len in graph[v]:
            candidate = path_len + edge_len
            if candidate < dist[w]:
                dist[w] = candidate
                heappush(queue, (candidate, w))

    return dist
