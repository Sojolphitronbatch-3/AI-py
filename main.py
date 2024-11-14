graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8', '9'],
    '2': [],
    '4': ['6'],
    '8':[],
    '9':[]
}

visited = []  # List for visited nodes
queue = []  # Initialize the queue

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)  # Remove the first element from the queue
        print(m, end=" ")  # Print the current node
        
        # Get the neighbors of the current node
        neighbours = graph.get(m, [])  # If the node is not found, return an empty list
        
        # Iterate over the neighbors of the current node
        for neighbour in neighbours:
            if neighbour not in visited:
                visited.append(neighbour)  # Mark as visited
                queue.append(neighbour)  # Add to the queue
                print("Following BFS")
                
# Start BFS from node '5'
bfs(visited, graph, '5')
