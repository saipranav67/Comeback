from collections import defaultdict

class GfG:
    def DFS1(self,u,adj,visited,st):
        visited[u]=True
        for v in adj[u]:
            if not visited[v]:
                self.DFS1(v,adj,visited,st)
        st.append(u)

    def DFS2(self,u,revAdj,visited,scc):
        visited[u]=True
        scc.append(u)
        for v in revAdj[u]:
            if not visited[v]:
                self.DFS2(v,revAdj,visited,scc)

    def kosaraju(self,V,adj):
        visited=[False]*V
        st=[]
        for i in range(V):
            if not visited[i]:
                self.DFS1(i,adj,visited,st)
        revAdj=[[] for _ in range(V)]
        for u in range(V):
            for v in adj[u]:
                revAdj[v].append(u)
        visited=[False]*V
        SCCs=[]
        while st:
            u=st.pop()
            if not visited[u]:
                scc=[]
                self.DFS2(u,revAdj,visited,scc)
                SCCs.append(scc)
        return SCCs

obj=GfG()
V=6
edges=[
    [0,1],[1,2],[2,0],
    [2,3],[3,4],[4,5],[5,3]
]

adj=[[] for _ in range(V)]
for u,v in edges:
    adj[u].append(v)

SCCs=obj.kosaraju(V,adj)
for scc in SCCs:
    for node in scc:
        print(node,end=" ")
    print()
