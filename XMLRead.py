import networkx as nx
import csv

import pandas as pd


Data = open('Datasets/Santander/public_devices/public_static_devices.csv', "r")
next(Data, None)  # skip the first line in the input file

Graphtype = nx.MultiGraph()
G = nx.parse_edgelist(Data, delimiter=',', create_using=Graphtype, nodetype=float, data=(('weight', float),))

#df = pd.read_csv('Datasets/Santander/public_devices/public_static_devices.csv')

#G = nx.from_pandas_edgelist(df, edge_attr='weight', create_using=Graphtype)

pos = nx.spring_layout(G.nodes)  # positions for all nodes

print(G)

nx.draw_networkx(G, pos=None)


list(G.nodes)
list(G.edges)
#list(G.adj[1])
#G.degree[1]

