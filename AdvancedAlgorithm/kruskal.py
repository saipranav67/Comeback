# Kruskal's Algorithm to find the Minimum Spanning Tree (MST)

# Class to represent a Union-Find (Disjoint Set) structure
class UnionFind:
    def __init__(self, n):
        # Each vertex is initially its own parent, and the rank is 0
        self.parent = [i for i in range(n)]  # Parent array
        self.rank = [0] * n  # Rank array

    # Find function with path compression
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    # Union function with union by rank
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        # If they belong to different sets, unite them
        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# Function to implement Kruskal's Algorithm
def kruskal(n, edges):
    # Step 1: Sort the edges by increasing weight
    edges.sort(key=lambda edge: edge[2])  # Sorting based on the weight of edges
    
    # Step 2: Create a UnionFind structure for the n vertices
    uf = UnionFind(n)
    
    # This will store the edges of the Minimum Spanning Tree (MST)
    mst = []
    
    # Step 3: Iterate over the sorted edges and build the MST
    for edge in edges:
        u, v, weight = edge
        
        # Step 3a: If u and v are in different sets, add this edge to the MST
        if uf.find(u) != uf.find(v):
            uf.union(u, v)  # Unite the sets containing u and v
            mst.append(edge)  # Add the edge to the MST
            
            # If we've added n-1 edges, we can stop (since the MST is complete)
            if len(mst) == n - 1:
                break
    
    return mst

# Example usage of Kruskal's Algorithm
if __name__ == "__main__":
    # Step 1: Define the number of vertices (n) and the list of edges
    n = 4  # Number of vertices
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    
    # Step 2: Call Kruskal's Algorithm to find the MST
    mst = kruskal(n, edges)
    
    # Step 3: Output the edges of the MST
    print("Edges in the Minimum Spanning Tree (MST):")
    total_weight = 0  # To keep track of the total weight of the MST
    
    for edge in mst:
        print(f"({edge[0]}, {edge[1]}) -> {edge[2]}")
        total_weight += edge[2]  # Add the weight of the edge to the total weight
    
    # Step 4: Print the total weight of the MST
    print(f"\nTotal weight of the Minimum Spanning Tree: {total_weight}")

