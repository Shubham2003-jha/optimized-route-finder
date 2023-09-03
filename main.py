import sys
from heapq import heappop, heappush
import matplotlib.pyplot as plt
import random

class Graph:
    def __init__(self):
        self.graph = {}
    def print(self):
        print(self.graph);

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
    def calculatedistance(self,start,end):
        ans=self.optimizedpath(start,end)
        distance=0
        for i in range(len(ans)-1):
            a=ans[i]
            b=ans[i+1]
            list=self.graph[a]
            for j in range(len(list)):
                tup=list[j]
                if(tup[0]==b):
                    distance+=tup[1]
        return distance
    def calculatetourlength(self,tour):
        n=len(tour)
        length=0
        for i in range(n-1):
            length+=self.calculatedistance(tour[i],tour[i+1])
        return length
    def perform_edge_exchange(self,i,j,tour):
        new_tour=tour[:i+1]+tour[i+1:j+1][::-1]+tour[j+1:]
        new_length=self.calculatetourlength(new_tour)
        return new_tour,new_length
    def lin_kernighan(self,tour):
        n=len(tour)
        tour_length = self.calculatetourlength(tour)
        improved = True
        while improved:
            improved=False
            for i in range(n):
                for j in range(i+2,n):
                    new_tour, new_length = self.perform_edge_exchange(i,j,tour)
                    if new_length < tour_length:
                        tour = new_tour
                        tour_length = new_length
                        improved = True
                        break
                if improved:
                    break

        return tour, tour_length
    def optimized_lin_kernighan(self,tour):
        length=self.calculatetourlength(tour)
        while(True):
            a,b=self.lin_kernighan(tour)
            if(b<length):
                tour=a
                length=b
            print(tour)
            print(length)
            break
        return tour,length
    def totalroute(self,tour):
        ans=[]
        for i in  range(len(tour)-1):
            x=tour[i]
            y=tour[i+1]
            l=self.optimizedpath(x,y)
            l.pop(-1)
            ans.extend(l)
        ans.append(tour[-1])
        return ans
    
class plot:
    def plotmap(self,coordinates,map_graph):
        plt.figure()
        for location, coord in coordinates.items():
            plt.plot(coord[0], coord[1],'bo')  # Plotting locations as blue circles
            plt.text(coord[0], coord[1] +0.1, location, ha='center')
        for location, connections in map_graph.graph.items():
            for neighbor, weight in connections:
                start_coord = coordinates[location]
                end_coord = coordinates[neighbor]
                plt.plot([start_coord[0], end_coord[0]], [start_coord[1], end_coord[1]], color='blue')  # Plotting connections as black lines
                plt.text((start_coord[0] + end_coord[0]) / 2, (start_coord[1] + end_coord[1]) / 2, str(weight), ha='right', color='green')  # Labeling connection weights
        plt.show()

    def plotlocal(self,coordinates,route_array,map_graph):
        plt.figure()
        for location, coord in coordinates.items():
            plt.plot(coord[0], coord[1],'bo')  # Plotting locations as blue circles
            plt.text(coord[0], coord[1] +0.1, location, ha='center')
        for i in range(len(route_array)-1):
            x=route_array[i]
            y=route_array[i+1]
            weight=-1
            for check in map_graph.graph[x]:
                if(check[0]==y):
                    weight=check[1]
                    break
            plt.plot([coordinates[x][0],coordinates[y][0] ], [coordinates[x][1], coordinates[y][1]], color='blue')  # Plotting connections as black lines
            plt.text((coordinates[x][0] + coordinates[y][0]) / 2, (coordinates[x][1] + coordinates[y][1]) / 2,str(weight), ha='right', color='green')  # Labeling connection weights
            

        plt.show()    


def graphinit():
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
    map_graph.add_connection("D", "E", 40)
    map_graph.add_connection("E", "F", 2)
    map_graph.add_connection("F", "G", 6)
    map_graph.add_connection("G", "H", 3)
    map_graph.add_connection("H", "I", 5)
    map_graph.add_connection("I", "J", 4)
    map_graph.add_connection("J", "K", 6)
    map_graph.add_connection("K", "L", 8)
    map_graph.add_connection("L", "M", 3)
    map_graph.add_connection("M", "N", 50)
    map_graph.add_connection("N", "O", 2)
    map_graph.add_connection("O", "P", 4)
    map_graph.add_connection("P", "Q", 6)
    map_graph.add_connection("Q", "R", 3)
    map_graph.add_connection("R", "S", 5)
    map_graph.add_connection("S", "T", 2)
    map_graph.add_connection("T", "U", 4)
    map_graph.add_connection("A", "D", 90)
    map_graph.add_connection("B", "E", 7)
    map_graph.add_connection("C", "F", 6)
    map_graph.add_connection("D", "G", 3)
    map_graph.add_connection("E", "H", 5)
    map_graph.add_connection("F", "I", 8)
    map_graph.add_connection("G", "J", 2)
    map_graph.add_connection("H", "K", 4)
    map_graph.add_connection("I", "L", 60)
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
    
    print("Enter 'Y' to see the map")
    a=input()
    if(a=='Y' or a=='y'):
        #print("yes")
        s=plot()
        s.plotmap(coordinates,map_graph)
        print("please enter")
        print("1: if u want to find shortest path between two points")
        print("2: if u want to find shortest path to cover multiple points ")
        x=int(input())
        if(x==1):
            print("You have choosen first option")
            print("Enter the 1st point : ",end='')
            a=input()
            print("Enter the 2nd point : ",end='')
            b=input()
            x=map_graph.optimizedpath(a,b)
            y=map_graph.calculatedistance(a,b)
            print("Distance of Fastest route is:",y,"units")
            print("Fastest Route: ",end='')
            print(x)
            localcoordinates={}
            for i in x:
                y=coordinates[i]
                localcoordinates[i]=y
            print("Enter Y to see the map of fastest route")
            a=input()
            if(a=='Y' or a=='y'):
                s.plotlocal(localcoordinates,x,map_graph)



    

    
graphinit()
