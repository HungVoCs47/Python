def dijkstra(graph, start_vertex):
    min_heap = new min_heap
    add_or_replace(min_heap, start_vertex, 0)
    while not(empty(min_heap)):
        v, distance  = remove(min_heap)
        for each i neighbor of v:
            distance_through_v = distance + graph[v][u]
            add_or_replace(min_heap, i, distance_through_v)
