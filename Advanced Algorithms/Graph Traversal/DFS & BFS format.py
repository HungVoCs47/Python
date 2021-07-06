def traversal(start_vertex, graph):
    queuing_structure = new_queuing_structure()
    queuing_structure.push(start_vertex, NULL)
    explored_vertices = []
    routing_table = []
    while queuing_structure is not empty:
        (current_vertex, parent ) = queuing_structure.pop()
        if not(current_vertex in explored_vertices):
            explored_vertices.push(current_vertex):
            routing_table[current_vertex]  = parent
            for neighbor in neighbors(graph, current_vertex):
                if neighbor not in explored_vertices:
                    queuing_structure.push(neighbor, current_vertex)
    return explored_vertices, routing_table
