def floydWarshall(dist):
    V=len(dist)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k]!=100000000 and dist[k][j]!=100000000:
                    dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])

INF=100000000
dist=[
    [0,3,INF,7],
    [8,0,2,INF],
    [5,INF,0,1],
    [2,INF,INF,0]
]

floydWarshall(dist)
for i in range(len(dist)):
    for j in range(len(dist)):
        print(dist[i][j],end=" ")
    print()
