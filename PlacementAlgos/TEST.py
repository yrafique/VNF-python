import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Define the number of nodes
num_iot_nodes = 20
num_access_points = 2
num_edge_servers = 4
 
#Define the locations of the access points and edge servers 
ap_locations = [(50, 50), (150, 50)]

server_locations = [(100, 100), (50, 150), (150, 150), (100, 200)]

# Create the graph
G = nx.Graph()

# Add the IoT nodes
for i in range(num_iot_nodes):
    G.add_node(i, location=(np.random.randint(0, 200), np.random.randint(0, 200)))

# Add the access points and edge servers
for i in range(num_access_points):
    G.add_node('AP{}'.format(i), location=ap_locations[i])
for i in range(num_edge_servers):
    G.add_node('Server{}'.format(i), location=server_locations[i])

# Connect the IoT nodes to the closest access point
iot_nodes = [i for i in range(num_iot_nodes)]
ap_nodes = ['AP{}'.format(i) for i in range(num_access_points)]
for i in iot_nodes:
    location = G.nodes[i]['location']
    distances = [np.sqrt((location[0]-G.nodes[ap]['location'][0])**2 + (location[1]-G.nodes[ap]['location'][1])**2) for ap in ap_nodes]
    closest_ap = ap_nodes[np.argmin(distances)]
    G.add_edge(i, closest_ap, weight=distances[np.argmin(distances)])


# Compute the distances from each node to the servers
for node in G.nodes():
    location = G.nodes[node]['location']
    distances = []
    for server in server_locations:
        if server in G.nodes():
            distance = np.sqrt((location[0]-G.nodes[server]['location'][0])**2 + (location[1]-G.nodes[server]['location'][1])**2)
            distances.append(distance)
    print(f"Distances for node {node}: {distances}")

# Connect the access points to the closest edge server
for ap in ap_nodes:
    location = G.nodes[ap]['location']
    distances = [np.sqrt((location[0]-G.nodes[server]['location'][0])**2 + (location[1]-G.nodes[server]['location'][1])**2) for server in server_locations]
    closest_server = 'Server{}'.format(np.argmin(distances))
    G.add_edge(ap, closest_server, weight=distances[np.argmin(distances)])

# Define the microservices and their requirements
microservices = {'object_detection': {'cpu': 0.5, 'memory': 1},
                 'face_recognition': {'cpu': 1, 'memory': 2},
                 'traffic_analysis': {'cpu': 2, 'memory': 4}}

# Assign microservices to the edge servers
for server in ['Server{}'.format(i) for i in range(num_edge_servers)]:
    server_cpu = 10
    server_memory = 16
    server_services = []
    while server_cpu >= 0 and server_memory >= 0:
        service = np.random.choice(list(microservices.keys()))
        service_cpu = microservices[service]['cpu']
        service_memory = microservices[service]['memory']
        if server_cpu - service_cpu >= 0 and server_memory - service_memory >= 0:
            server_cpu -= service_cpu
            server_memory -= service_memory
            server_services.append(service)
    G.nodes[server]['services'] = server_services

# Plot the graph
pos = nx.get_node_attributes(G, 'location')
nx.draw(G, pos)
nx.draw_networkx_labels(G, pos)

# Measure the end-to-end delay for a given IoT device
iot_device = np.random.choice(iot_nodes)
iot_location = G.nodes[iot_device]['location']
ap_node = [n for n in G.neighbors(iot_device) if n.startswith('AP')][0]
    # Identify server nodes within range of access points
server_nodes = [n for n in G.neighbors(ap_node) if n not in iot_nodes]
servers_within_range = []
for s in server_nodes:
        distance = np.sqrt((location[0]-G.nodes[s]['location'][0])**2 + (location[1]-G.nodes[s]['location'][1])**2)
        if distance <= range:
            servers_within_range.append(s)

        # If there are no servers within range, skip this IoT node
        if not servers_within_range:
            continue 

    # Calculate the cost for each server within range
costs = []
for s in servers_within_range:
    total_cost = 0
    # Calculate cost for each microservice
    for service in microservices:
            # Calculate the distance from the server to the cloud server running the microservice
            cloud_server = service['cloud_server']
            cloud_server_location = G.nodes[cloud_server]['location']
            cloud_server_distance = np.sqrt((G.nodes[s]['location'][0]-cloud_server_location[0])**2 + (G.nodes[s]['location'][1]-cloud_server_location[1])**2)
            # Calculate the cost of the microservice on the server
            cost = (service['size']/bandwidth)*1000 + cloud_server_distance*(1/propagation_speed)*1000
            total_cost += cost
            costs.append(total_cost)

    # Assign IoT node to the server with the lowest cost
    min_cost_index = np.argmin(costs)
    min_cost_server = servers_within_range[min_cost_index]
    G.nodes[iot_node]['assigned_server'] = min_cost_server

# Plot the network
pos = nx.get_node_attributes(G, 'location')
nx.draw(G, pos, node_color='lightblue', with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

# Measure end-to-end delay
# Calculate the total end-to-end delay

total_delay = 0
for iot_node in iot_nodes:
    server_node = G.nodes[iot_node]['assigned_server']
    total_delay += nx.shortest_path_length(G, iot_node, server_node, weight='weight')

print(f"Total end-to-end delay: {total_delay}ms")

