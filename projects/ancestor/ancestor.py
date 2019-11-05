from graph import Graph
from util import Stack


def find_ancestors(ancestors, starting_node):
    # create an empty list ancestors
    direct_ancestors = []
    # loop through the input list of tuples
    for parent, child in ancestors:
        # see if the child is starting_node
        if child == starting_node:
            # add the parent to direct_ancestors
            direct_ancestors.append(parent)

    # if direct_ancestors is empty return -1
    if not len(direct_ancestors):
        return -1
    # otherwise, return direct_ancestors
    else:
        return direct_ancestors


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

    # create a stack to hold the vertices
    s = Stack()
    # add the starting_node to the stack
    s.push(starting_node)

    # loop while stack is not empty
    while s.size() > 0:
        # pop the stack
        vertex = s.pop()

        # add all its connected vertices to the queue
        for v in graph.vertices[vertex]:
            s.push(v)


if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6),
                      (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

    print(find_ancestors(test_ancestors, 3))  # output should be [1, 2]
    print(find_ancestors(test_ancestors, 1))  # should output [1]
    print(find_ancestors(test_ancestors, 11))  # should output [-1]
