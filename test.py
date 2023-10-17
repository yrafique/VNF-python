# %% [markdown]
# Network X Code goes here, now we convert it into a graph

# %%


# %%
##Instal packages ex: python3.11 -m pip install pandas  

# Importing required libraries
import random
import networkx as nx   # for creating and manipulating graphs
import matplotlib.pyplot as plt   # for visualizing graphs

# Importing required functions
import PerformanceAnalysis.MeasureStatistics as MeasureStatistics  # to measure network statistics
import SearchAlgos.PageRank as  PageRank  # to compute node rankings based on pagerank

# Importing a user-defined function to read network data from XML file
from Import_NetworkFromXML_backup import *

# Defining a function to convert nodes in the XML network dictionary to nodes in networkx graph
def convert_nodes (G, nodes):
    for node in nodes:
        node_id = nodes[node].get("id")
        x_cor = nodes[node].get("x_cor")
        y_cor = nodes[node].get("y_cor")
        G.add_node(node_id, pos=(x_cor, y_cor))

# Defining a function to convert links in the XML network dictionary to edges in networkx graph
def convert_links (G, nodes, links):
    for link in links.keys():
        source = links[link].get("source")
        for source_node in nodes:
            if nodes[source_node].get('id') == source:
                break
        dest = links[link].get("destination")
        for dest_node in nodes:
            if nodes[dest_node].get('id') == dest:
                break
        capacity = links[link].get("capacity")
        cost = links[link].get("cost")
        G.add_edges_from([(source, dest, {'capacity': capacity, 'cost': cost})])

# Defining a function to convert demands in the XML network dictionary to networkx graph
def convert_demands(G, nodes, demands):    
    a = 1

# Defining a function to create random users in the networkx graph
def create_users (G, nodes):
    for node in nodes:
        node_id = nodes[node].get("id")
        x_cor = nodes[node].get("x_cor")
        y_cor = nodes[node].get("y_cor")
        randx = random.randint(x_cor,x_cor+x_cor*2)
        randy = random.randint(y_cor,y_cor+y_cor*2)
        print(randx)
        print(randy)

# Defining the name of the network and creating an empty networkx graph
network_name = "abilene.xml"
G = nx.Graph()

# Defining the path to the network XML file and reading the network data from the file
path = 'Networks/'
from_xml = read_XMLnetwork (path+network_name)

# Extracting nodes, links, and demands data from the network data dictionary
nodes = from_xml[0]
links = from_xml[1]
demands = from_xml[2]

# Converting nodes and links data to nodes and edges in networkx graph
convert_nodes(G,nodes)
convert_links(G,nodes,links)

# Calculating shortest paths between all pairs of nodes in the networkx graph
sp = dict(nx.all_pairs_shortest_path(G))

# Drawing the networkx graph with node positions and other attributes
nx.draw(G, nx.get_node_attributes(G, 'pos'), with_labels=True, node_size=300, style = "solid")

# calling the measure_statistics function and passing the networkx graph G as a parameter
MeasureStatistics.topology_statistics(G)

# calling the assortativity_measure function and passing the networkx graph G as a parameter
MeasureStatistics.assortativity_measure(G)

pagerank_df = PageRank.compute_pagerank(G)
print("Page Rank Weights")
print(pagerank_df)

# %% [markdown]
# # Approximations and Heuristics
# Approximations of graph properties and Heuristic methods for optimization.
# 
# # import
# These functions can be accessed using networkx.approximation.function_name
# 
# They can be imported using from networkx.algorithms import approximation or from networkx.algorithms.approximation import function_name
# 
# # Treewidth
# Functions for computing treewidth decomposition.
# 
# Treewidth of an undirected graph is a number associated with the graph. It can be defined as the size of the largest vertex set (bag) in a tree decomposition of the graph minus one.
# 
# Wikipedia: Treewidth
# 
# treewidth_min_degree(G): Returns a treewidth decomposition using the Minimum Degree heuristic.

# %% [markdown]
# ## To Implement:
# 1. Generate Users: Randomly distrubuted users generated with uniform random distrubution of (x,y) corrdinates around the graph G that represents infrastrcuture. Allow options (ex. User_Spread).
# 2. Connect each user to nearest AP: Allow options (ex. SNR, Connected_Users, Access_Technology).
# 3. Generate demand for each user: Assign User -> Application (Define SFCn = {VNF1 + VNF2 + .... + VNFx}).
# 4. Create Placement Algorithm for each Placement Solution.
# 5. Create a Next Candidate Search Algorithm: Takes as an input (G, Users, Demamds).
# 6. Measure network statistics for each Placement Algorithm.
# 7. Generate logs for each Placement Algorithm.
# 8. Save logs in an output file.
# 9. Create function to plot from the logs.

# %% [markdown]
# ## Generate Users
# Here we will generate users
# 
# Generate Users: Randomly distrubuted users generated with uniform random distrubution of (x,y) corrdinates around the graph G that represents infrastrcuture. 
# 
# Allow options (ex. User_Spread).

# %%
#users

# (1) Create a new graph, G_users, to represent the users.
G_users = nx.Graph()

# (2, 3) Modify the create_users function to add user nodes to G_users and add NoOfUsers parameter
def create_users(G, G_users, nodes, NoOfUsers):
    user_count = 0
    while user_count < NoOfUsers:
        for node in nodes:
            node_id = nodes[node].get("id")
            x_cor = nodes[node].get("x_cor")
            y_cor = nodes[node].get("y_cor")

            # Use random.uniform() instead of random.randint() and convert the result to an integer
            randx = int(random.uniform(x_cor - 2.5, x_cor + 2.5))
            randy = int(random.uniform(y_cor - 2.5, y_cor + 2.5))

            user_id = "user_" + str(user_count)
            G_users.add_node(user_id, pos=(randx, randy))
            user_count += 1

            if user_count >= NoOfUsers:
                break


# (5) Call the create_users function with the desired number of users
NoOfUsers = 100
create_users(G, G_users, nodes, NoOfUsers)

# Draw the original graph G and the graph of users G_users together
pos_G = nx.get_node_attributes(G, 'pos')
pos_G_users = nx.get_node_attributes(G_users, 'pos')

nx.draw(G, pos_G, with_labels=True, node_size=300, style="solid", node_color="blue")
nx.draw(G_users, pos_G_users, with_labels=False, node_size=100, style="dashed", node_color="red", alpha=0.5)

plt.show()

# %% [markdown]
# # Add Edge Device Attributes
# 

# %%
# (1) Import the json module
import json

# (2) Load the JSON data from the EdgeDevices.json file
with open("Devices/EdgeDevices.json", "r") as file:
    edge_devices_data = json.load(file)

# (3) Create a function to associate edge devices with their attributes
def associate_edge_devices(G, edge_devices_data):
    edge_devices = edge_devices_data["edgeDevices"]
    edge_servers = edge_devices_data["edgeServers"]

    for node in G.nodes():
        device = random.choice(edge_devices + edge_servers)
        G.nodes[node]["name"] = device["name"]
        G.nodes[node]["formFactor"] = device["formFactor"]
        G.nodes[node]["architecture"] = device["architecture"]
        G.nodes[node]["cpu"] = device["cpu"]
        G.nodes[node]["memory"] = device["memory"]
        G.nodes[node]["storage"] = device["storage"]
        G.nodes[node]["source"] = device["source"]

# (4) Call the function to update the attributes of the edge devices in the graph
associate_edge_devices(G, edge_devices_data)

#Debug to print
for node, attrs in G.nodes(data=True):
    print(f"Node: {node}")
    for attr_key, attr_value in attrs.items():
        print(f"  {attr_key}: {attr_value}")
    print()


# %%
from scipy.spatial.distance import euclidean
import random
import networkx as nx
import matplotlib.pyplot as plt

# ... (other functions you've already defined) ...

# Function to find the nearest AP for a given user position
def find_nearest_ap(G, user_pos):
    min_distance = float('inf')
    nearest_ap = None
    nearest_pos = None

    for ap, pos in nx.get_node_attributes(G, 'pos').items():
        distance = euclidean(user_pos, pos)
        if distance < min_distance:
            min_distance = distance
            nearest_ap = ap
            nearest_pos = pos

    return nearest_ap, nearest_pos

# Updated create_users function to track user connections
def create_users(G, G_users, nodes, NoOfUsers):
    user_connections = []
    user_count = 0
    while user_count < NoOfUsers:
        for node in nodes:
            node_id = nodes[node].get("id")
            x_cor = nodes[node].get("x_cor")
            y_cor = nodes[node].get("y_cor")
            randx = int(random.uniform(x_cor - 2.5, x_cor + 2.5))
            randy = int(random.uniform(y_cor - 2.5, y_cor + 2.5))

            user_pos = (randx, randy)
            nearest_ap, nearest_pos = find_nearest_ap(G, user_pos)

            user_id = "user_" + str(user_count)
            G_users.add_node(user_id, pos=user_pos)
            user_connections.append((user_pos, nearest_pos))

            user_count += 1
            if user_count >= NoOfUsers:
                break

    return user_connections

# (rest of the existing code)

# ...
# Create a new graph for users and call create_users
G_users = nx.Graph()
NoOfUsers = 500
user_connections = create_users(G, G_users, nodes, NoOfUsers)

# Draw the graphs and user connections
pos_G = nx.get_node_attributes(G, 'pos')
pos_G_users = nx.get_node_attributes(G_users, 'pos')

nx.draw(G, pos_G, with_labels=True, node_size=300, style="solid", node_color="blue")
nx.draw(G_users, pos_G_users, with_labels=False, node_size=100, style="dashed", node_color="red", alpha=0.5)

# Draw the connections between users and APs
for user_pos, ap_pos in user_connections:
    plt.plot([user_pos[0], ap_pos[0]], [user_pos[1], ap_pos[1]], color="green", linestyle="-")

plt.show()

# ... (rest of the existing code)



