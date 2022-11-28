from random import randint
import pandas as pd
import networkx as nx
from time import time
import numpy as np

import matplotlib.pyplot as plt


filename = 'abilene.xml'
G = nx.read_graphml(filename, node_type = int)



G = nx.read_graphml(filename)

nx.draw_networkx(G, with_labels=True)
plt.axis('off')
plt.show()

print(type(G), G)
# (<class 'networkx.classes.digraph.DiGraph'>, <networkx.classes.digraph.DiGraph object at 0x10e29c150>)

print(nx.shortest_path(G, 1, 5))
#[1, 2, 3, 4, 5]


""" 

df = pd.DataFrame()
df['a'] = [randint(0, 15) for _ in range(100)]

print(df)
df['b'] = [randint(0, 15) for _ in range(100)]
#G=nx.from_pandas_edgelist(df, 'idA', 'idB', ['amount'])
c = 0
runs = []
while c <= 100:
    G=nx.Graph()
    start = time()
    for i in df.index:
        G.add_node(df['a'][i], name = df['a'][i])
        G.add_node(df['b'][i], name = df['b'][i])
        G.add_edge(df['a'][i], df['b'][i])

    run = time() - start
    runs.append(run)
    c += 1

print ('done in:', np.mean(runs), 'seconds')


c = 0
runs = []
while c <= 100:
    G=nx.Graph()
    start = time()
    G=nx.from_pandas_edgelist(df, 'a', 'b')
    run = time() - start
    runs.append(run)
    c += 1

print(G)
nx.draw(G)
plt.show()

print ('done in:', np.mean(runs), 'seconds')

"""
