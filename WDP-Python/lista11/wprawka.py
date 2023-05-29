def in_graph(graph, para):
    a = para[0]
    b = para[1]
    
    if a not in graph:
        return False
    
    for g in graph[a]:
        if g == b:
            return True
    return False

def add_to_graph(a,b,graph):
    if a not in graph:
        graph[a] = set()
    graph[a] = graph[a].add(b)

class Graph:
    def __init__(self, *elems): #elems to zbior par
        self.graph = {}
        for a,b in elems:
            if elems not in self:
                self.graph[a] = set()
            tmp = self[a]
            tmp.add(b)
            self.graph[a] = tmp
            
    def add(self, a,b):
        add_to_graph(a,b, self.graph)    
        
    def __contains__(self, para):
        return in_graph(self.graph, para) 
        
    def __str__(self):
        return f'Graph({self.graph})'
    
    def __eq__(self, other):
    
        if len(self) != len(other):
            return False
        for key in self:
            if key not in other:
                return False
            else:
                if len(self[key]) != len(other[key]):
                    return False
                else:
                    for val in self[key]:
                        if val not in other[key]:
                            return False
        return True      
            
    def __or__(self, other):
        new = Graph()

        for key in self.graph:
            new[key] = self[key]
        for key in other.graph:
            if key not in new:
                new[key] = other[key]
            else:
                new[key] = new[key] | other[key]
        return new  

graf = Graph((1,2),(2,3),(1,4))
print(graf)