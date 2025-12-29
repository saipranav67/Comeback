import heapq  # For priority queue (min-heap)

# Prim's Algorithm to find the Minimum Spanning Tree (MST)
def prim(n, graph):
    # Initialize the MST and the min-heap
    in_mst = [False] * n  # To keep track of vertices already in MST
    min_edge = [(0, 0)]  # (weight, vertex) - start from vertex 0 with weight 0
    mst = []  # To store edges in the MST
    total_weight = 0  # To store the total weight of the MST
    
    # We use a min-heap to always pick the minimum weight edge
    # The heap will store tuples (weight, (start, end)) where:
    # - weight is the edge's weight
    # - (start, end) are the vertices the edge connects
    heapq.heapify(min_edge)

    while min_edge:
        # Extract the minimum weight edge from the heap
        weight, u = heapq.heappop(min_edge)
        
        # If the vertex is already in MST, skip it
        if in_mst[u]:
            continue
        
        # Mark the vertex as included in MST
        in_mst[u] = True
        total_weight += weight  # Add edge weight to total weight
        
        # Add the edge to the MST (u is the vertex just added)
        if weight > 0:  # Ignore the first dummy edge (0, 0)
            mst.append((u, weight))
        
        # Add all edges from u to the heap that connect to vertices not in the MST
        for v, weight in graph[u]:
            if not in_mst[v]:
                heapq.heappush(min_edge, (weight, v))  # Add the edge to the priority queue

    return mst, total_weight

# Example usage:
if __name__ == "__main__":
    # Number of vertices
    n = 5
    # Represent the graph as an adjacency list
    # graph[u] contains a list of tuples (v, weight) where u-v is an edge with a given weight
    graph = {
        0: [(1, 2), (3, 6), (4, 7)],
        1: [(0, 2), (2, 3), (3, 8)],
        2: [(1, 3), (4, 5)],
        3: [(0, 6), (1, 8), (4, 9)],
        4: [(0, 7), (2, 5), (3, 9)]
    }

    # Run Prim's algorithm to find the MST and its total weight
    mst, total_weight = prim(n, graph)

    # Print the edges in the MST
    print("Edges in the Minimum Spanning Tree (MST):")
    for u, weight in mst:
        print(f"Vertex {u} is connected with weight {weight}")
    
    # Print the total weight of the MST
    print(f"\nTotal weight of the Minimum Spanning Tree: {total_weight}")
