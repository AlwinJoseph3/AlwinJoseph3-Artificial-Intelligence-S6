def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        if node in graph:
            for neighbor in graph[node]:
                dfs(visited, graph, neighbor)

# Step 1: Read the number of vertices from the user
vertices = int(input("Enter the number of vertices: "))

# Step 2: Read graph edges (source destination) from the user
graph = {}
print("Enter the edges in the format 'source destination':")
for _ in range(vertices):
    edge = input().split()
    source, destination = edge[0], edge[1]
    if source not in graph:
        graph[source] = []
    graph[source].append(destination)

# Step 3: Create a set for storing visited nodes
visited = set()

# Step 4: Display final DFS result
print("DFS Traversal:")
dfs(visited, graph, next(iter(graph)))  # Start DFS from the first node in the graph
