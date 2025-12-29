adj= [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
q=[]
res=[]
v=[False]*len(adj)
src=0
q.append(src)
v[src]=True
while len(q)!=0:
    cur=q.pop(0)
    res.append(cur)
    for i in adj[cur]:
         if(v[i]==False):
            q.append(i)
            v[i]=True
print(res)


