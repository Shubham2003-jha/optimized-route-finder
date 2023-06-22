import sys
from heapq import heappop, heappush
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = {}

    def add_location(self, location):
        self.graph[location] = []

    def add_connection(self, location1, location2, weight):
        if location1 in self.graph and location2 in self.graph:
            self.graph[location1].append((location2, weight))
            self.graph[location2].append((location1, weight))
        else:
            print("Invalid locations!")

    def dijkstra(self, start_location):
        distances={location: sys.maxsize for location in self.graph}
        distances[start_location]=0
        heap=[(0,start_location)]
        while(heap):
            curr_distance,curr_location=heappop(heap)
            if(curr_distance>distances[curr_location]):
                continue
            for location,weight in self.graph[curr_location]:
                if(curr_distance+weight<distances[location]):
                    distances[location]=curr_distance+weight
                    heappush(heap,(curr_distance+weight,location))
        return distances
    def optimizedpath(self,start,end):
        ans=[]
        parent={location:location for location in self.graph}
        distances={location: sys.maxsize for location in self.graph}
        distances[start]=0
        heap=[(0,start)]
        while(heap):
            curr_distance,curr_location=heappop(heap)
            if(curr_distance>distances[curr_location]):
                continue
            for location,weight in self.graph[curr_location]:
                if(curr_distance+weight<distances[location]):
                    parent[location]=curr_location
                    distances[location]=curr_distance+weight
                    heappush(heap,(curr_distance+weight,location))
        node=end
        while(parent[node]!=node):
            ans.insert(0,node)
            node=parent[node]
        ans.insert(0,node)
        return ans


        pass


map_graph = Graph()

#================================================================================================================
map_graph.add_location("A")
map_graph.add_location("B")
map_graph.add_location("C")
map_graph.add_location("D")
map_graph.add_location("D")
map_graph.add_location("E")
map_graph.add_location("F")
map_graph.add_location("G")
map_graph.add_location("H")
map_graph.add_location("I")
map_graph.add_location("J")
map_graph.add_location("K")
map_graph.add_location("L")
map_graph.add_location("M")
map_graph.add_location("N")
map_graph.add_location("O")
map_graph.add_location("P")
map_graph.add_location("Q")
map_graph.add_location("R")
map_graph.add_location("S")
map_graph.add_location("T")
map_graph.add_location("U")

#-----------------------------------------------------------------------------------------------
map_graph.add_connection("A", "B", 5)
map_graph.add_connection("B", "C", 3)
map_graph.add_connection("C", "D", 2)
map_graph.add_connection("D", "E", 4)
map_graph.add_connection("E", "F", 2)
map_graph.add_connection("F", "G", 6)
map_graph.add_connection("G", "H", 3)
map_graph.add_connection("H", "I", 5)
map_graph.add_connection("I", "J", 4)
map_graph.add_connection("J", "K", 6)
map_graph.add_connection("K", "L", 8)
map_graph.add_connection("L", "M", 3)
map_graph.add_connection("M", "N", 5)
map_graph.add_connection("N", "O", 2)
map_graph.add_connection("O", "P", 4)
map_graph.add_connection("P", "Q", 6)
map_graph.add_connection("Q", "R", 3)
map_graph.add_connection("R", "S", 5)
map_graph.add_connection("S", "T", 2)
map_graph.add_connection("T", "U", 4)
map_graph.add_connection("A", "D", 9)
map_graph.add_connection("B", "E", 7)
map_graph.add_connection("C", "F", 6)
map_graph.add_connection("D", "G", 3)
map_graph.add_connection("E", "H", 5)
map_graph.add_connection("F", "I", 8)
map_graph.add_connection("G", "J", 2)
map_graph.add_connection("H", "K", 4)
map_graph.add_connection("I", "L", 6)
map_graph.add_connection("J", "M", 7)
map_graph.add_connection("K", "N", 4)
map_graph.add_connection("L", "O", 5)
map_graph.add_connection("M", "P", 3)
map_graph.add_connection("N", "Q", 5)
map_graph.add_connection("O", "R", 6)
map_graph.add_connection("P", "S", 4)
map_graph.add_connection("Q", "T", 3)
map_graph.add_connection("R", "U", 2)

#=================================================================================================================
coordinates = {
    "A": (0, 0),
    "B": (1, 1),
    "C": (2, 0),
    "D": (1, -1),
    "E": (0, -2),
    "F": (2, -2),
    "G": (3, -1),
    "H": (4, -2),
    "I": (4, -1),
    "J": (3, 0),
    "K": (5, 0),
    "L": (6, 1),
    "M": (7, 0),
    "N": (8, 1),
    "O": (9, 0),
    "P": (10, 1),
    "Q": (11, 0),
    "R": (10, -1),
    "S": (9, -2),
    "T": (11, -2),
    "U": (12, -1)
}
plt.figure()
for location, coord in coordinates.items():
    plt.plot(coord[0], coord[1],'bo')  # Plotting locations as blue circles
    plt.text(coord[0], coord[1] +0.1, location, ha='center')

for location, connections in map_graph.graph.items():
    for neighbor, weight in connections:
        start_coord = coordinates[location]
        end_coord = coordinates[neighbor]
        plt.plot([start_coord[0], end_coord[0]], [start_coord[1], end_coord[1]], color='black')  # Plotting connections as black lines
        plt.text((start_coord[0] + end_coord[0]) / 2, (start_coord[1] + end_coord[1]) / 2, str(weight), ha='right', color='green')  # Labeling connection weights
plt.show()
ans=map_graph.optimizedpath('B','U');
print(ans)
