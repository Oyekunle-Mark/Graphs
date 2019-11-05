from graph import Graph
from util import Stack


def earliest_ancestor(ancestors, starting_node):
    # FIRST REPRESENT THE INPUT ANCESTORS AS A GRAPH
    graph = Graph()

    # loop through ancestors and add the tuples as vertices
    for parent, child in ancestors:
        # add the parent as a vertex
        graph.add_vertex(parent)
        # add the child as a vertex as well
        graph.add_vertex(child)

    # # loop through ancestors and build the connections
    for parent, child in ancestors:
        # connect the parent to the child
        graph.add_edge(child, parent)

    # return -1 if input has no value
    if not graph.vertices[starting_node]:
        return -1

    # create a stack to hold the vertices
    s = Stack()
    # add the starting_node to the stack
    s.push(starting_node)
    # set earliest_anc to -1
    earliest_anc = -1

    # loop while stack is not empty
    while s.size() > 0:
        # pop the stack
        vertex = s.pop()
        # print the vertex
        # print(vertex)

        # set the earliest_anc to vertex
        earliest_anc = vertex

        # add all its connected vertices to the queue
        # sort the vertices to the order is maintained
        for v in sorted(graph.vertices[vertex]):
            s.push(v)

    return earliest_anc
