import sys
class Graph():
    def __init__(self, vertex):
        self.V = vertex
        self.graph = [[0 for column in range(vertex)] for row in range(vertex)]

    def printSolution(self, dist):
        print ("Vertex distance from source")
        for node in range(self.V):
            print (node, " ", dist[node])

    def minDistance(self, dist, spots):
        # Initilaize minimum distance for next node
        min = sys.maxsize
        # Search not nearest vertex not in the shortest path tree
        for v in range(self.V):
            if dist[v] < min and spots[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        spots = [False] * self.V
        for cout in range(self.V):
            u = self.minDistance(dist, spots)
            spots[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and spots[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        # self.printSolution(dist)
        return dist

# g = Graph(9)
# g.graph = [
#     [0, 4, 0, 0, 0, 0, 0, 8, 0],
#     [4, 0, 8, 0, 0, 0, 0, 7, 0],
#     [0, 8, 0, 7, 0, 4, 0, 0, 2],
#     [0, 0, 7, 0, 9, 8, 0, 0, 0],
#     [0, 0, 0, 9, 0, 9, 0, 0, 0],
#     [0, 0, 4, 8, 9, 0, 2, 0, 0],
#     [0, 0, 0, 0, 0, 2, 0, 1, 6],
#     [8, 7, 0, 0, 0, 0, 1, 0, 7],
#     [0, 0, 2, 0, 0, 0, 6, 7, 0]
# ]
# g.dijkstra(0)
