from util import Stack, Queue


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    # BFT

    def bft(self, starting_vertex_id):
        # create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex_id)
        # create a set to store the visited vertices
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # if that vertex has not been visited
            if v not in visited:
                # mark it as visited (printing for a representation)
                print(v)
                visited.add(v)
                # then add all of it's neighbors to the back of the queue
                for next_vertex in self.vertices[v]:
                    q.enqueue(next_vertex)

    # DFT
    def dft(self, starting_vertex_id):
        # create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex_id)
        # create a set to store the visited vertices
        visited = set()
        # while the stack is not empty
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()
            # if that vertex has not been visited
            if v not in visited:
                # mark it as visited (printing for a representation)
                print(v)
                visited.add(v)
                # then add all of it's neighbors to the top of the stack
                for next_vertex in self.vertices[v]:
                    s.push(next_vertex)

    def dft_recursive(self, start_vert, visited=None):
        # if the visited structure is set to None
        if visited is None:
            # create a new set for visited
            visited = set()

        # add a starting vertex to the visited set
        visited.add(start_vert)
        # print the start vertex
        print(start_vert)
        # loop over every child vertex in vertices set at the start vertex
        for child_vert in self.vertices[start_vert]:
            # if child vertex is not in visited
            if child_vert not in visited:
                # do a recursive call to dft_recursive
                # using the child vertex and the current visited set as arguments
                self.dft_recursive(child_vert, visited)

    def dfs(self, start_vert, target_value, visited=None):
        # if visited is None
        if visited is None:
            # create a new set of visited
            visited = set()
        # add start vert to visited
        visited.add(start_vert)
        # if the start vert is equal to the target value
        if start_vert == target_value:
            # return True
            return True
        # loop over every child vertex in vertices set at the start vertex
        for child_vert in self.vertices[start_vert]:
            # if child vert is not in visited
            if child_vert not in visited:
                # if the recursive call to dfs
                if self.dfs(child_vert, target_value, visited):
                    # return True
                    return True
        # Return False
        return False

    def bfs(self, starting_vertex_id, target_value):
        # create a queue to hold the vertex ids
        q = Queue()
        # enqueue the start vertex id
        q.enqueue(starting_vertex_id)
        # create an empty visited set
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # set vert to the dequeued element
            vert = q.dequeue()
            # if the vert is not in visited
            if vert not in visited:
                # if vert is target value
                if vert == target_value:
                    # return True
                    return True
                # add the vert to visited set
                visited.add(vert)
                # loop over next vert in the vertices at the index of vert
                for next_vert in self.vertices[vert]:
                    # enqueue the next vert
                    q.enqueue(next_vert)
        # return False
        return False

    def bfs_path(self, starting_vertex_id, target_value):
        # create a queue
        q = Queue()
        # enqueue a list holding the starting vertex id
        q.enqueue([starting_vertex_id])
        # created an empty visited set
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # dequeue to the path
            path = q.dequeue()
            # set a vert to the last item in the path
            vert = path[-1]
            # if vert is not in visited
            if vert not in visited:
                # if vert is equal to target value
                if vert == target_value:
                    # return path
                    return path
                # add vert to visited set
                visited.add(vert)
                # loop over next vert in vertices at the index of vert
                for next_vert in self.vertices[vert]:
                    # set a new path equal to a new list of the path (copy)
                    new_path = list(path)
                    # append next vert to new path
                    new_path.append(next_vert)
                    # enqueue the new path
                    q.enqueue(new_path)
        # return None
        return None

    def dfs_path(self, starting_vertex_id, target_value):
        # create a stack
        s = Stack()
        # push a list holding the starting vertex id
        s.push([starting_vertex_id])
        # created an empty visited set
        visited = set()
        # while the queue is not empty
        while s.size() > 0:
            # pop to the path
            path = s.pop()
            # set a vert to the last item in the path
            vert = path[-1]
            # if vert is not in visited
            if vert not in visited:
                # if vert is equal to target value
                if vert == target_value:
                    # return path
                    return path
                # add vert to visited set
                visited.add(vert)
                # loop over next vert in vertices at the index of vert
                for next_vert in self.vertices[vert]:
                    # set a new path equal to a new list of the path (copy)
                    new_path = list(path)
                    # append next vert to new path
                    new_path.append(next_vert)
                    # push the new path
                    s.push(new_path)
        # return None
        return None
