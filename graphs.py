from collections import deque
import heapq


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, start, end, distance=0):
        if start not in self.nodes:
            self.nodes[start] = {}
        if end not in self.nodes:
            self.nodes[end] = {}
        self.nodes[start][end] = distance
        self.nodes[end][start] = distance

    def print_nodes(self):
        print(self.nodes)

    def dfs(self, start, visited=None):
        if visited == None:
            visited = set()
        visited.add(start)
        print(start)
        for neighbor in self.nodes[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            visited.add(node)
            print(node)
            for neighbor in self.nodes[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.nodes}
        distances[start] = 0
        queue = [(0, start)]
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            print(">< "+ current_node)
            if current_distance > distances[current_node]:
                continue
            for neighbor, distance in self.nodes[current_node].items():
                print(">> " + neighbor)
                new_distance = current_distance + distance
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(queue, (new_distance, neighbor))
                    print(queue)
        print(distances)


a = Graph()

a.add_edge("A", "B", 1)
a.add_edge("B", "C", 2)
a.add_edge("A", "D", 4)
a.add_edge("G", "D", 1)
a.add_edge("D", "B", 5)
a.add_edge("E", "F", 1)


a.print_nodes()

a.dijkstra("A")
