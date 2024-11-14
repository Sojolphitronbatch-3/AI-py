def bfs_path(graph, start, goal):
    # Initialize the visited set, queue, and parent map
    visited = []  
    queue = []  
    parent = {}  # Dictionary to track the parent of each node

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)  # Pop the first element from the queue

        # If we reached the goal, reconstruct the path
        if node == goal:
            path = []
            while node is not None:  # Trace back from goal to start
                path.append(node)
                node = parent.get(node)  # Get the parent node
            return path[::-1]  # Return the reversed path (start -> goal)

        # Explore the neighbors of the current node
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                parent[neighbour] = node  # Set the current node as parent of the neighbor

    return None  # Return None if no path is found

# Driver code
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8', '9'],
    '2': [],
    '4': ['6'],
    '8': [],
    '9': [],
    '6': []
}

start = '5'
goal = '8'

path = bfs_path(graph, start, goal)
if path:
    print("Path from", start, "to", goal, ":", path)
else:
    print("No path found from", start, "to", goal)
