from collections import defaultdict
from collections import deque
# import networkx as nx
# import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt
# import networkx as nx
# import random

def calculate_renovations(original_counts, new_counts):
    # Calculate histograms of original and new connection counts
    original_histogram = defaultdict(int)
    new_histogram = defaultdict(int)
    
    for count in original_counts.values():
        original_histogram[count] += 1
    for count in new_counts.values():
        new_histogram[count] += 1
    
    # Calculate the number of renovations based on the histogram differences
    renovations = 0
    for count in set(original_histogram.keys()).union(new_histogram.keys()):
        renovations += abs(original_histogram[count] - new_histogram[count])
    
    return renovations // 2


def redesign_floorplan(n, m, edges):
    # Count the number of connections for each room
    original_connection_count = defaultdict(int)
    for i, j in edges:
        original_connection_count[i] += 1
        original_connection_count[j] += 1

    # Separate leaf nodes (with one connection) from others
    leaf_nodes = set(node for node, count in original_connection_count.items() if count == 1)
    non_leaf_nodes = set(range(n)) - leaf_nodes

    # Sort non-leaf nodes by their connection counts (fewer connections first)
    sorted_non_leaf_nodes = sorted(non_leaf_nodes, key=lambda x: original_connection_count[x])

    # Create a new layout with a central path using sorted non-leaf nodes
    new_edges = []
    current_connection_count = defaultdict(int)
    current_target = deque()
    for i in range(1, len(sorted_non_leaf_nodes)):
        if i == 1:
            target_0 = sorted_non_leaf_nodes[0]
            current_target.append((target_0, original_connection_count[target_0] - 1))
        else:
            target = current_target[0]
            target_0 = target[0]
            amount = target[1] - 1
            if amount == 0:
                current_target.popleft()  # Efficiently removes the leftmost item
            else:
                current_target[0] = (target[0], amount)
        a, b = sorted_non_leaf_nodes[i], target_0
        new_edges.append((a, b))
        current_connection_count[a] += 1
        current_connection_count[b] += 1
        current_target.append((a, original_connection_count[a] - 1))
    
    # resort based on how close the node is to oringal_connection_count
    sorted_non_leaf_nodes = sorted(sorted_non_leaf_nodes, key=lambda x: abs(original_connection_count[x] - current_connection_count[x]))


    # Connect leaf nodes to the central path, filling up the required connections
    for non_leaf in sorted_non_leaf_nodes:
        while current_connection_count[non_leaf] < original_connection_count[non_leaf] and leaf_nodes:
            leaf = leaf_nodes.pop()
            new_edges.append((non_leaf, leaf))
            current_connection_count[non_leaf] += 1
            current_connection_count[leaf] += 1

    while leaf_nodes:
        leaf1 = leaf_nodes.pop()
        leaf2 = leaf_nodes.pop()
        new_edges.append((leaf1, leaf2))
        current_connection_count[leaf1] += 1
        current_connection_count[leaf2] += 1
    
    # Count the rooms that need renovation
    renovated_rooms = calculate_renovations(original_connection_count, current_connection_count)

    # check for still unconnected leaf nodes
    # connect them with each other


    return renovated_rooms, new_edges


    # Count the rooms that need renovation
    # A room needs renovation if its new connection count differs from the original
    # renovated_rooms = 0
    # new_connection_count = defaultdict(int)
    # for i, j in new_edges:
    #     new_connection_count[i] += 1
    #     new_connection_count[j] += 1

    # for node in range(n):
    #     if new_connection_count[node] != connection_count[node]:
    #         renovated_rooms += 1

    # return renovated_rooms, new_edges

# Solve with the final approach

# def visualize_tree(tree_edges):
#     # Create a graph from the tree edges
#     G = nx.Graph()
#     G.add_edges_from(tree_edges)

#     # Draw the graph
#     plt.figure(figsize=(8, 6))
#     nx.draw(G, with_labels=True, node_color='lightblue', node_size=700, font_size=10, font_weight='bold', edge_color='gray')
#     plt.title("Tree Visualization")
#     plt.show()
# Sample Input
# n, m = 7, 8
# edges = [(0, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (0, 5), (0, 3)]
# sample_output_edges = [
#     (1, 2), 
#     (5, 6),
#     (0, 1),
#     (0, 3),
#     (0, 5)
# ]


# visualize_tree([(0, 1), (0, 2), (0, 4), (1, 3), (1, 4), (2, 3)])
# visualize_tree(edges) 
# visualize_tree(sample_output_edges)
# # Solve
# renovated_rooms, new_edges = redesign_floorplan(n, m, edges)
# # visualize_tree(new_edges)
# # print(renovated_rooms, new_edges)

# print(renovated_rooms)
# for new_edge in new_edges:
#     print(*new_edge)

def parse_input():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    return n, m, edges

def main():
    n, m, edges = parse_input()
    renovated_rooms, new_edges = redesign_floorplan(n, m, edges)
    print(renovated_rooms)
    print(n, len(new_edges))
    for edge in new_edges:
        print(*edge)

main()

# from itertools import combinations
# import networkx as nx

# def is_tree(G):
#     """ Check if a graph G is a tree """
#     return nx.is_connected(G) and G.number_of_edges() == G.number_of_nodes() - 1

# def calculate_renovated_rooms(original_graph, new_graph):
#     """ Calculate the number of rooms that need renovation """
#     renovations = 0
#     for node in original_graph.nodes():
#         original_edges = set(original_graph.edges(node))
#         new_edges = set(new_graph.edges(node))
#         # Count the room if the number of exits changes
#         if len(original_edges) != len(new_edges):
#             renovations += 1
#     return renovations

# def brute_force_solution_with_room_count(n, original_edges):
#     # Create the original graph
#     original_graph = nx.Graph()
#     original_graph.add_nodes_from(range(n))
#     original_graph.add_edges_from(original_edges)

#     # Generate all possible graphs
#     min_renovations = float('inf')
#     optimal_graph = None
#     for edges in combinations(combinations(range(n), 2), n - 1):
#         G = nx.Graph()
#         G.add_nodes_from(range(n))
#         G.add_edges_from(edges)

#         # Check if the generated graph is a tree
#         if is_tree(G):
#             # Calculate renovations needed
#             renovations = calculate_renovated_rooms(original_graph, G)
#             if renovations < min_renovations:
#                 min_renovations = renovations
#                 optimal_graph = G

#     return optimal_graph, min_renovations

# def generate_erdos_renyi_graph(n, p):
#     """
#     Generate a random Erdős-Rényi graph.

#     Parameters:
#     n (int): Number of nodes in the graph.
#     p (float): Probability for edge creation.

#     Returns:
#     G (networkx.Graph): A random Erdős-Rényi graph.
#     """
#     G = nx.erdos_renyi_graph(n, p)

#     # Ensure the graph is connected; if not, regenerate
#     while not nx.is_connected(G):
#         G = nx.erdos_renyi_graph(n, p)

#     return G

# example = [(0, 1), (0, 2), (0, 4), (1, 3), (1, 4), (2, 3)]
example = [(0, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (0, 5), (0, 3)]
# example = [(0, 2), (0, 3), (0, 4), (1, 3), (2, 3), (2, 4), (3, 4)]
# example = [(0, 2), (0, 3), (0, 4), (1, 2), (2, 4), (3, 4)]
# example =[(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
# 1 2
# 1 3
# 1 4
# 1 5
# 1 6
# 0 5
# 0 3
# # example = [(0, 1)]
# visualize_tree(example)

# graph, n_rooms = brute_force_solution_with_room_count(7, example)
# edges_graph = graph.edges()
# visualize_tree(edges_graph)
# print(n_rooms)
# nn, edges_2 = redesign_floorplan(7, len(example), example)
# visualize_tree(edges_2)
# print(nn)

# print(redesign_floorplan(2, 1, [(0, 1)]))
# for i in range(1000):
#     n = random.randint(1, 5)
#     p = 0.3
#     G = generate_erdos_renyi_graph(n, p)
#     edges = list(G.edges())
#     _, amount = brute_force_solution_with_room_count(n, edges)
#     amount2, _ = redesign_floorplan(n, len(edges), edges)
#     if amount != amount2:
#         print(n, amount, amount2, edges)
#         break
#     else:
#         print("OK")