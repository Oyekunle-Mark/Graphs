"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # check if both v2 and v1 are vertices in self.vertices
        if v1 in self.vertices and v2 in self.vertices:
            # add v2 to self.vertices at index v1
            self.vertices[v1].add(v2)
        # otherwise
        else:
            # raise an exception
            raise KeyError(f"You need to add {v1} and {v2} as vertices first")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a queue to hold the vertices
        q = Queue()
        # add the starting_vertex to the queue
        q.enqueue(starting_vertex)
        # let a set store the visited vertices
        visited = set()

        # loop while queue is not empty
        while q.size() > 0:
            # dequeue the queue
            vertex = q.dequeue()

            # if the  dequeued vertex is not in visited
            if vertex not in visited:
                # add to visited
                visited.add(vertex)
                # print the vertex
                print(vertex)

                # add all its connected vertices to the queue
                for v in self.vertices[vertex]:
                    q.enqueue(v)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack to hold the vertices
        s = Stack()
        # add the starting_vertex to the stack
        s.push(starting_vertex)
        # let a set store the visited vertices
        visited = set()

        # loop while stack is not empty
        while s.size() > 0:
            # pop the stack
            vertex = s.pop()

            # if the popped vertex is not in visited
            if vertex not in visited:
                # add to visited
                visited.add(vertex)
                # print the vertex
                print(vertex)

                # add all its connected vertices to the queue
                for v in self.vertices[vertex]:
                    s.push(v)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # create a stack to hold the vertices
        s = Stack()
        # add the starting_vertex to the stack
        s.push(starting_vertex)
        # let a set store the visited vertices
        visited = set()

        # create a recursive function recurse_dft
        def recurse_dft():
            # write a base case of size of stack is zero
            if s.size() == 0:
                # return
                return

            # pop the vertex at the top of the stack
            vertex = s.pop()

            # if the popped vertex is not in visited
            if vertex not in visited:
                # add to visited
                visited.add(vertex)
                # print the vertex
                print(vertex)

                # add all its connected vertices to the queue
                for v in self.vertices[vertex]:
                    s.push(v)

            # call recurse_dft
            recurse_dft()

        # call recurse_dft
        recurse_dft()

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue to hold the vertices
        q = Queue()
        # enqueue the starting_vertex
        q.enqueue(starting_vertex)
        # create an empty list visited to store visited vertices
        visited = []
        # create an empty set searched to store searched vertices
        searched = set()

        # loop while queue is not empty
        while q.size() > 0:
            # dequeue the queue
            vertex = q.dequeue()

            # check if the vertex has not been searched
            if vertex not in searched:
                # if the dequeued vertex is the destination
                if vertex == destination_vertex:
                    # add it to visitied
                    visited.append(vertex)
                    # return visited
                    return visited

                # otherwise
                else:
                    # add it to searched
                    searched.add(vertex)
                    # add it to visited
                    visited.append(vertex)

                    # add all its vertices to the queue
                    for v in self.vertices[vertex]:
                        # if one of them is the destination
                        if v == destination_vertex:
                            # add to visited
                            visited.append(v)
                            # return visited
                            return visited
                        # otherwise
                        else:
                            # enqueue v
                            q.enqueue(v)

        # return False if not found
        return False

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create a stack to hold the vertices
        s = Stack()
        # add the starting_vertex
        s.push(starting_vertex)
        # create an empty list visited to store visited vertices
        visited = []
        # create an empty set searched to store searched vertices
        searched = set()

        # loop while stack is not empty
        while s.size() > 0:
            # pop the stack
            vertex = s.pop()

            # check if the vertex has not been searched
            if vertex not in searched:
                # if the popped vertex is the destination
                if vertex == destination_vertex:
                    # add it to visitied
                    visited.append(vertex)
                    # return visited
                    return visited

                # otherwise
                else:
                    # add it to searched
                    searched.add(vertex)
                    # add it to visited
                    visited.append(vertex)

                    # add all its vertices to the stack
                    for v in self.vertices[vertex]:
                        # if one of them is the destination
                        if v == destination_vertex:
                            # add to visited
                            visited.append(v)
                            # return visited
                            return visited
                        # otherwise
                        else:
                            # push v
                            s.push(v)

        # return False if not found
        return False

    def find_path(self, vertices):
        """Will take a list of visited vertices and construct the shortest
        path from it

        Arguments:
            vertices {list} -- list of visited vertices

        Returns:
            list -- the shortest path
        """
        # get the destination vertex
        destination_vertex = vertices[-1]
        # create a new list containing destination vertex to store path
        path = [destination_vertex]

        # loop backward
        for i in range(len(vertices) - 2, -1, -1):
            # if the vertex before does not connect with destination vertex
            if destination_vertex not in self.vertices[vertices[i]]:
                # continue
                continue
            # otherwise,
            else:
                # add it to the list
                path.append(vertices[i])
                # set the current vertex to the destination
                destination_vertex = vertices[i]

        # reverse path
        path.reverse()
        # return path
        return path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    print("\nVertices are:")
    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    print("\nDFT print:")
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    print("\nBFT print:")
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    print("\nRecursive BFT print:")
    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    print("\nBFS print:")
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    print("\nDFS print:")
    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
