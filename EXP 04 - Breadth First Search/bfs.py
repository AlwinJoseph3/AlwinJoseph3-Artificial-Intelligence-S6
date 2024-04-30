from collections import defaultdict

def bfs(graph, start):
    visited = []  # List to keep track of visited nodes
    queue = []  # Initialize a queue

    queue.append(start)
    visited.append(start)

    while queue:
        current_node = queue.pop(0)
        print(current_node, end=' ')

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)

graph = defaultdict(list)

vertices = int(input("Enter the number of vertices: "))
print("Enter the edges(source  destination)")
for _ in range(vertices):
    edge = input().split()
    graph[edge[0]].append(edge[1])

start_node = input("Enter the starting node for BFS: ")

print("BFS Traversal:")
bfs(graph, start_node)
