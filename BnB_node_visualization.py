import networkx as nx
import matplotlib as plt

# Code to visualize connectivity and path using NetworkX
def visualize_graph_networkx(nodeNetwork, tour, dfs_result):
    G = nx.Graph()

    # Add edges with distances
    for i in range(len(nodeNetwork)):
        for j in range(i + 1, len(nodeNetwork)):
            G.add_edge(i, j, weight=nodeNetwork[i, j])

    pos = nx.spring_layout(G)  # Layout for better visualization

    # Plot graph
    nx.draw(G, pos, with_labels=True, font_weight='bold')

    # Highlight tour edges
    tour_edges = [(tour[i-1], tour[i]) for i in range(1, len(tour))]
    nx.draw_networkx_edges(G, pos, edgelist=tour_edges, edge_color='blue', width=2)

    # Highlight DFS edges
    dfs_edges = [(dfs_result[i-1], dfs_result[i]) for i in range(1, len(dfs_result))]
    nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, edge_color='red', width=2)

    # Highlight starting node
    nx.draw_networkx_nodes(G, pos, nodelist=[0], node_color='green', node_size=200)

    plt.title('Graph Visualization')
    plt.show()

# Run DFS
dfs_stack = [start_node]
dfs_result = depth_first_search(start_node, nodeNetwork, [], dfs_stack)

# Print DFS Result
print("DFS Result:", dfs_result)

visualize_graph_networkx(nodeNetwork, bnb_result, dfs_result)