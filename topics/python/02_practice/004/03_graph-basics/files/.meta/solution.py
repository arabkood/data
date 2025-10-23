from collections import deque


class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, v1, v2):
        if v1 not in self.graph:
            self.add_vertex(v1)
        if v2 not in self.graph:
            self.add_vertex(v2)

        self.graph[v1].append(v2)
        if not self.directed:
            self.graph[v2].append(v1)

    def get_neighbors(self, vertex):
        return self.graph.get(vertex, [])

    def has_path(self, start, end):
        if start not in self.graph or end not in self.graph:
            return False

        visited = set()
        queue = deque([start])

        while queue:
            current = queue.popleft()
            if current == end:
                return True

            if current in visited:
                continue

            visited.add(current)
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

        return False
