from collections import defaultdict

class Graph():

    def __init__(self):
        self.elements = defaultdict(list)

    # adjacent list
    def addEdge(self, vertex, edge):
        self.elements[vertex].append(edge)


    def depth_first_search_traverse(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")

        for next_vertex in self.elements[vertex]:
            if next_vertex not in visited:
                self.depth_first_search_traverse(next_vertex, visited)
        print("")

    
    def depth_first_search(self, vertex):
        visited = set()
        self.depth_first_search_traverse(vertex, visited)


    def breadth_first_search(self, vertex):
        visited = set()
        queue = [vertex]
        
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for next_vertex in self.elements[vertex]:
                if next_vertex not in visited:
                    queue.append(next_vertex)
                    visited.add(next_vertex)
        print("")


    def topological_sort_traverse(self, vertex, visited, stack):
        visited.add(vertex)

        for next_vertex in self.elements[vertex]:
            if next_vertex not in visited:
                self.topological_sort_traverse(next_vertex, visited, stack)

        stack.append(vertex) 


    def topological_sort(self):
        visited = set()
        stack = list()

        # for vertex in self.elements.keys():
        #     if vertex not in visited:
        #         self.topological_sort_traverse(self.elements.keys()[1], visited, stack)

        self.topological_sort_traverse(list(self.elements.keys())[0], visited, stack)
        print(reversed(stack))

if __name__ == "__main__":
    graph = Graph()
    graph.addEdge(0, 1) 
    graph.addEdge(0, 2) 
    graph.addEdge(1, 2) 
    graph.addEdge(2, 0) 
    graph.addEdge(2, 3) 
    graph.addEdge(3, 3) 

    graph.depth_first_search(2)
    graph.breadth_first_search(2)

    g= Graph() 
    g.addEdge(5, 2); 
    g.addEdge(5, 0); 
    g.addEdge(4, 0); 
    g.addEdge(4, 1); 
    g.addEdge(2, 3); 
    g.addEdge(3, 1); 


    g.topological_sort()