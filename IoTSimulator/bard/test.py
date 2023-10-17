import networkx as nx
import matplotlib.pyplot as plt
import geopandas as gpd
import random

def read_graph_from_file(file_path):
    G = nx.Graph()
    with open(file_path, 'r') as f:
        for line in f:
            if not line.startswith('#'):  # Skip comments
                i, j, bandwidth = map(float, line.strip().split())
                G.add_edge(int(i), int(j), weight=bandwidth)
    return G

def read_ingress_nodes(file_path):
    ingress_nodes = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line.startswith('#'):  # Skip comments
                ingress_nodes.extend(map(int, line.split()))
    return ingress_nodes

# File paths
graph_file_path = 'graph.txt'
ingress_file_path = 'ingress.txt'

# Read the graph and ingress nodes
G = read_graph_from_file(graph_file_path)
ingress_nodes = read_ingress_nodes(ingress_file_path)

# Generate mock coordinates
for node in G.nodes():
    G.nodes[node]['lat'] = random.uniform(45.45, 45.47)
    G.nodes[node]['lon'] = random.uniform(9.18, 9.20)

# Print the graph and ingress nodes
print("Nodes in Graph:", list(G.nodes))
print("Edges in Graph:", list(G.edges(data=True)))
print("Ingress Nodes:", ingress_nodes)

# Plotting the network topology
pos = nx.spring_layout(G, seed=42)
normal_nodes = [node for node in G.nodes if node not in ingress_nodes]

nx.draw(G, pos, with_labels=True, nodelist=normal_nodes, node_color='blue', node_size=700, font_size=16)
nx.draw(G, pos, with_labels=True, nodelist=ingress_nodes, node_color='red', node_size=700, font_size=16)

labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12)

plt.title('Network Topology')
plt.show()
