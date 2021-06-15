class Graph:
    def __init__(self, v):
        self.edges=[[0]*v for i in range(v)]
        self.v=v
    def add_edge(self, a, b):
        self.edges[a][b]=1
    def remove_edge(self, a, b):
        self.edges[a][b]=0
    def get_v(self):
        return self.v
    def is_edge(self, a, b):
        return self.edges[a][b]==1
    def get_path(self, a, b, path=[], visit=[], start=True):
        if start:
            visit=[False]*self.v
            path=[]
        visit[a]=True
        if a==b:
            path.append(a)
            return path
        for i in range(self.v):
            if self.edges[a][i]==1 and not visit[i]:
                path.append(a)
                result=self.get_path(i, b, path, visit, start=False)
                if result!=False:
                    return result
                path.pop()
        return False
    def remove_path(self, path):
        for i in range(len(path)-1):
            self.remove_edge(path[i], path[i+1])
            self.add_edge(path[i+1], path[i])

def edge_disjoint_paths(graph, s, t):
    result_graph=Graph(graph.v)
    path1=graph.get_path(s, t, start=True)
    if path1==False:
        print("No edge disjoint paths found!")
        return
    graph.remove_path(path1)
    path2=graph.get_path(s, t, start=True)
    if path1==False:
        print("No edge disjoint paths found!")
        return
    for i in range(len(path1)-1):
        result_graph.add_edge(path1[i], path1[i+1])
    for i in range(len(path2)-1):
        if result_graph.is_edge(path2[i+1], path2[i]):
            result_graph.remove_edge(path2[i+1], path2[i])
        else:
            result_graph.add_edge(path2[i], path2[i+1])
    result1=result_graph.get_path(s, t, start=True)
    print("Path 1 is: "+" ".join([str(node) for node in result1]))
    result_graph.remove_path(result1)
    result2=result_graph.get_path(s, t, start=True)
    print("Path 2 is: "+" ".join([str(node) for node in result2]))

if __name__ == "__main__":
    n, m=map(int, input("Enter count of nodes and edges:(n m) ").split())
    graph=Graph(n)
    print("Enter edges in each line:(a b)")
    for i in range(m):
        a, b=map(int,input().split())
        graph.add_edge(a, b)
    s, t=map(int,input("Enter s, t:(s t) ").split())
    edge_disjoint_paths(graph, s, t)
