from graph import Graph
from util import Stack


def earliest_ancestor(ancestors, starting_node):
    # FIRST REPRESENT THE INPUT ANCESTORS AS A GRAPH
    # create a graph instance
    graph = Graph()

    # loop through ancestors and add every number as a vertex
    for parent, child in ancestors:
        # add the parent as a vertex
        graph.add_vertex(parent)
        # add the child as a vertex as well
        graph.add_vertex(child)

    # # loop through ancestors and build the connections
    for parent, child in ancestors:
        # connect the parent to the child
        # the connection is reversed because dft transverses downward
        graph.add_edge(child, parent)

    # if starting node has no child
    if not graph.vertices[starting_node]:
        # return -1
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

        # set the earliest_anc to vertex
        earliest_anc = vertex

        # add all its connected vertices to the queue
        # sort the vertices maintain order
        for v in sorted(graph.vertices[vertex]):
            s.push(v)

    return earliest_anc
