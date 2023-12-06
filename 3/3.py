from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

def find_spanning_tree(n, edges):
    # Function to create a spanning tree using BFS
    def bfs(start):
        visited = set()
        tree = []
        queue = [start]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                queue.extend(graph[node] - visited)
                tree.extend((node, v) for v in graph[node] if v not in visited)
        return tree

    # Creating a graph from the edges
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    # Finding a spanning tree
    spanning_tree = bfs(0)  # assuming the graph is connected and starting from node 0

    # Counting the number of modified rooms
    modified_rooms = sum(1 for i in range(n) if len(graph[i]) != 1)

    return modified_rooms, spanning_tree

def visualize_tree(tree_edges):
    # Create a graph from the tree edges
    G = nx.Graph()
    G.add_edges_from(tree_edges)

    # Draw the graph
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color='lightblue', node_size=700, font_size=10, font_weight='bold', edge_color='gray')
    plt.title("Tree Visualization")
    plt.show()

def is_valid_tree(edges):
    # Create a graph from the edges
    graph = nx.Graph()
    graph.add_edges_from(edges)

    # Check if the graph is a tree
    # A graph is a tree if it is connected and has n-1 edges
    is_tree = nx.is_tree(graph)
    
    return is_tree


# We can test this function with the new floorplan we generated earlier
# However, we know that it won't be valid since it was not a correct tree


# Sample input
n, m = 7, 8
edges = [(0, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (0, 5), (0, 3)]

# Find the spanning tree and the count of modified rooms
modified_rooms, new_floorplan = find_spanning_tree(n, edges)

sample_output_edges = [
    (1, 2), 
    (5, 6),
    (0, 1),
    (0, 3),
    (0, 5)
]
print(is_valid_tree(sample_output_edges))

# modified_rooms, new_floorplan

# visualize_tree(edges)
# visualize_tree(new_floorplan)
