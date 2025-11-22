def dijkstra(graph, start):
    # Number of nodes
    n = len(graph)
    
    # Initialize distances to infinity
    distances = [float('inf')] * n
    distances[start] = 0  # Distance to the start node is 0
    
    # Priority queue: list of (distance, node) tuples
    pq = [(0, start)]  # Start with the source node (distance, node)
    
    while pq:
        # Find the node with the smallest distance (like extracting from a priority queue)
        pq.sort()  # Sort the list to simulate a priority queue
        current_distance, current_node = pq.pop(0)  # Pop the first element (smallest distance)
        
        # If the node has already been visited, skip it
        if current_distance > distances[current_node]:
            continue
        
        # Explore the neighbors
        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight
            
            # If a shorter path is found, update the distance and add the neighbor to the queue
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                pq.append((new_distance, neighbor))  # Add to the priority queue
                
    return distances

# Example graph as an adjacency list:
# graph[node] = [(neighbor, weight), ...]
# graph = [
#     [(1, 2), (2, 4)],  # Node 0 is connected to Node 1 with weight 2, and Node 2 with weight 4
#     [(0, 2), (2, 1), (3, 7)],  # Node 1 is connected to Node 0 with weight 2, Node 2 with weight 1, and Node 3 with weight 7
#     [(0, 4), (1, 1), (3, 3)],  # Node 2 is connected to Node 0 with weight 4, Node 1 with weight 1, and Node 3 with weight 3
#     [(1, 7), (2, 3)]   # Node 3 is connected to Node 1 with weight 7, and Node 2 with weight 3
# ]
graph = [[[1, 4], [2, 8]],         
                                            [[0, 4], [4, 6], [2,3]], 
                                            [[0, 8], [3, 2], [1,3]], 
                                            [[2, 2], [4, 10]], 
                                            [[1, 6], [3, 10]]]

start_node = 0  # Start from node 0

# Get the shortest distances from the start node
distances = dijkstra(graph, start_node)

print(f"Shortest distances from node {start_node}: {distances}")
