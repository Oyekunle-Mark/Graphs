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
