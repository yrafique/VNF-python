# Importing required libraries
import networkx as nx
import numpy as np
import pandas as pd

# Function to calculate and print the topology statistics of a given graph
def topology_statistics(G):
    print("Topology Stats:")
    # Calculate and print graph density
    print('Density:', nx.density(G))
    # Calculate and print average shortest path length
    print('Avg. shortest path length:', nx.average_shortest_path_length(G))
    # Calculate and print average clustering coefficient
    print('Avg. clustering coefficient:', nx.average_clustering(G))
    # Calculate and print assortativity coefficient
    print('Assortativity', nx.degree_assortativity_coefficient(G))

# Function to calculate and print the assortativity measure for a given graph
def assortativity_measure(G):
    print("\nAssortativity Stats:")
    # Initialize lists to store assortativity values for Erdos-Renyi and configuration model random graphs
    erdos_assortativity_list = list()
    conf_assortativity_list = list()

    # Calculate the number of nodes and probability of edge creation
    n = G.number_of_nodes() # number of nodes
    p = 2.*G.number_of_edges()/(n*n-1) # probability of edge creation
    print(n)
    print(p)

    # Calculate the degree distribution of the input graph
    degree_dist = np.asarray(list(dict(G.degree()).values()))

    # Loop 100 times to create random graphs and calculate assortativity
    for i in range(100): 
        # Create Erdos-Renyi random graph
        erdos_rg = nx.erdos_renyi_graph(n, p, seed=np.random.randint(10))
        # Create configuration model random graph and convert it to a simple graph
        conf_rg = nx.Graph(nx.configuration_model(degree_dist, seed=np.random.randint(10)))
        # Calculate assortativity and append to the respective lists
        erdos_assortativity_list.append(nx.degree_assortativity_coefficient(erdos_rg))
        conf_assortativity_list.append(nx.degree_assortativity_coefficient(conf_rg))

    # Print average and standard deviation of assortativity values for Erdos-Renyi and configuration model random graphs
    print('Erdos-Renyi assortativity:', np.mean(erdos_assortativity_list), np.std(erdos_assortativity_list, ddof=1))
    print('Conf. model assortativity:', np.mean(conf_assortativity_list), np.std(conf_assortativity_list, ddof=1))
    # Print the assortativity value of the input graph
    print('Real network value:', nx.degree_assortativity_coefficient(G))
    print("")

# The assortativity measure shows the tendency of nodes with similar degrees to connect to each other.
# A higher value indicates that low-degree nodes (members) tend to connect with high-degree nodes (leaders),
# suggesting a core-periphery or leader-member structure in the network.
# However, this simple approach does not provide definitive proof of such a structure.
