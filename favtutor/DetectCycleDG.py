from collections import defaultdict

# Function to perform DFS traversal
def DFS(graph, node, visited, rec_stack):
    # Mark the current node as visited and add it to the recursion stack
    visited[node] = True
    rec_stack[node] = True

    # Recur for all the neighboring vertices
    for neighbor in graph[node]:
        # If neighbor is not visited, then recur for it
        if not visited[neighbor]:
            if DFS(graph, neighbor, visited, rec_stack):
                return True
        # If neighbor is already visited and present in recursion stack, then cycle exists
        elif rec_stack[neighbor]:
            return True

    # Remove the node from recursion stack
    rec_stack[node] = False
    return False

# Function to detect cycle in directed graph using DFS
def detect_cycle_DFS(graph):
    # Create a visited set and a recursion stack
    visited = {node: False for node in graph}
    rec_stack = {node: False for node in graph}

    # Perform DFS traversal for all nodes to detect cycle
    for node in graph:
        if not visited[node]:
            if DFS(graph, node, visited, rec_stack):
                return True

    return False

# Example directed graph
graph = {
    'A': ['B'],
    'B': ['C', 'E'],
    'C': [],
    'D': ['A', 'E'],
    'E': ['D']
}

# Detect cycle in graph using DFS
if detect_cycle_DFS(graph):
    print("Cycle exists in graph")
else:
    print("Cycle does not exist in graph")

'''To detect cycles in this graph using BFS, we start by initializing an empty queue and a visited set. We then enqueue the starting node and mark it as visited. 
We then repeatedly dequeue nodes from the queue and add all their unvisited neighbors to the queue, marking them as visited.
While doing this, we keep track of the parent node for each node we visit, so that we can trace back the path to any cycle we find.
Starting at node A, we enqueue it and mark it as visited. We then dequeue node A and add its neighbors B and D to the queue. 
We mark both B and D as visited and set their parent nodes as A. We continue dequeuing and enqueuing nodes until the queue becomes empty.
Now, let's suppose we start the BFS traversal again, but this time starting at node E instead of A. We enqueue node E and mark it as visited. 
We then dequeue node E and add its neighbors B and D to the queue. However, B is already in the visited set, and its parent node is not E, but A.
Therefore, we know that there exists a cycle in the graph, which is A -> B -> E -> D -> A.
Thus, by performing BFS on the directed graph, we were able to detect the cycle in the graph.
'''
