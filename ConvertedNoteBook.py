import networkx as nx
import matplotlib.pyplot as plt
import random
from Import_NetworkFromXML_backup import read_XMLnetwork
import math

def convert_nodes(G, nodes):
    for node in nodes:
        node_id = nodes[node].get("id")
        x_cor = nodes[node].get("x_cor")
        y_cor = nodes[node].get("y_cor")
        G.add_node(node_id, pos=(float(x_cor), float(y_cor)))

def convert_links(G, nodes, links):
    for link in links.keys():
        source = links[link].get("source")
        dest = links[link].get("destination")
        capacity = links[link].get("capacity")
        cost = links[link].get("cost")
        G.add_edge(source, dest, capacity=float(capacity), cost=float(cost))

network_name = "abilene.xml"
G = nx.Graph()
path = 'Networks/'
from_xml = read_XMLnetwork(path+network_name)

nodes = from_xml[0]
links = from_xml[1]

convert_nodes(G, nodes)
convert_links(G, nodes, links)

# print network info
print(nx.info(G))

# draw the network
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True, node_size=300)

# generate users
NoOfUsers = 100
G_users = nx.Graph()

# distribute users across the infrastructure
max_x = max([float(nodes[node].get("x_cor")) for node in nodes])
min_x = min([float(nodes[node].get("x_cor")) for node in nodes])
max_y = max([float(nodes[node].get("y_cor")) for node in nodes])
min_y = min([float(nodes[node].get("y_cor")) for node in nodes])

for u in range(NoOfUsers):
    randx = round(random.uniform(min_x, max_x), 2)
    randy = round(random.uniform(min_y, max_y), 2)
    G_users.add_node(u, pos=(randx, randy))

# draw the users
pos_users = nx.get_node_attributes(G_users, 'pos')
nx.draw(G_users, pos_users, with_labels=True, node_size=300, style="solid", edge_color="skyblue")

# function to calculate Euclidean distance
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

for u in G_users.nodes():
    pos = nx.get_node_attributes(G, 'pos')
    print(pos)
    nearest_ap = min(G_users.nodes, key=lambda x: euclidean_distance(pos[x], pos[u]))
    #nearest_ap = min(G.nodes, key=lambda x: euclidean_distance(pos[x][0], pos[u][1]))
    nearest_aps.append(nearest_ap)

#Now we have a list of nearest APs for each user, we can use this information to calculate the signal strength
signal_strengths = []
for i, u in enumerate(G_users.nodes()):
    signal_strength = euclidean_distance(pos[nearest_aps[i]][0], pos[nearest_aps[i]][1])
    signal_strengths.append(signal_strength)

#The final step is to plot the signal strength for each user
plt.scatter(G_users.nodes(), signal_strengths)
plt.xlabel('Users')
plt.ylabel('Signal Strength')
plt.show()

#This code will create a scatter plot of signal strength for each user, with the x-axis showing the users and the y-axis showing the signal strength.
#You can adjust the code to suit your specific needs and data.
