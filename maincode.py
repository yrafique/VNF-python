
# Imported network_classes.py
# network_classes.py
# Here we define all network-related classes used to represent different components of a network.

class Node:
    """
    Represents a node in the network.
    
# Application: Car - Slice1
# Slice1: SFC1 + SFC2 + SFC3
# SFC1: Firewall  + router
        y (float): The y-coordinate of the node in the network diagram.
    """
print("[DEBUG 1] Entering function: __init__")
def __init__(self, uid, x, y):
        """Initialize a new Node instance."""
        self.uid = uid
        self.x = x
        self.y = y
        
        class Link:
print("[DEBUG 2] Exiting function: __init__")
    """
    Represents a link between two nodes in the network.
    
    Attributes:
        uid (str): Unique identifier for the link.
        source (str): UID of the source node.
        target (str): UID of the target node.
        capacity (float): The capacity of the link (e.g., in Mbps).
        cost (float): The cost associated with using the link.
        propagation_delay (float): The latency (e.g., in ms) based on the propagation delay.
    """
print("[DEBUG 3] Entering function: __init__")
def __init__(self, uid, source, target, capacity, cost, propagation_delay=0):
        """Initialize a new Link instance."""
        self.uid = uid
        self.source = source
        self.target = target
        self.capacity = capacity
        self.cost = cost
        self.propagation_delay = propagation_delay
        
        class Demand:
print("[DEBUG 4] Exiting function: __init__")
    """
    Represents a demand from one node to another in the network.
    
    Attributes:
        uid (str): Unique identifier for the demand.
        source (str): UID of the source node.
        destination (str): UID of the destination node.
        demandValue (float): The amount of demand from source to destination (e.g., in Mbps).
    """
print("[DEBUG 5] Entering function: __init__")
def __init__(self, uid, source, destination, demandValue):
        """Initialize a new Demand instance."""
        self.uid = uid
        self.source = source
        self.destination = destination
        self.demandValue = demandValue
        
        class Server:
print("[DEBUG 6] Exiting function: __init__")
    """
    Represents a server in the network.
    
    Attributes:
        name (str): The name of the server model.
        formFactor (int): The form factor of the server, typically a numerical value indicating size or capacity.
        architecture (str): The CPU architecture type of the server, typically indicating the instruction set architecture such as x86 or ARM.
        cpu (str): The CPU specification of the server, typically indicating speed and core count.
        memory (str): The memory capacity of the server, typically specified in GB or TB.
        storage (str): The storage capacity of the server, typically specified in TB.
        source (str): The data source or the specific model identifier for the server.
        server_cost (float): The cost or price of the server, typically in units of currency.
    """
print("[DEBUG 7] Entering function: __init__")
def __init__(self, name, formFactor, architecture, cpu, memory, storage, source, server_cost):
        """Initialize a new Server instance."""
        self.name = name
        self.formFactor = formFactor
        self.architecture = architecture
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.source = source
        self.server_cost = server_cost
        
        class User:
print("[DEBUG 8] Exiting function: __init__")
    """
    Represents a user device in the network.
    
    Attributes:
        id (str): Identifier for the user.
        pos (tuple): The (x, y) coordinates of the user device.
        associated_ap (str): The Access Point the user is connected to.
        application (Application): The application assigned to the user. Initially None until assigned.
        measured_bw (float): The measured bandwidth for the user. Initially 0.0 and updated later.
        measured_delay (float): The measured delay for the user. Initially 0.0 and updated later.
        associated_app (str): The application associated with the user. Initially None until assigned.
    """
print("[DEBUG 9] Entering function: __init__")
def __init__(self, user_id, pos, associated_ap):
        """Initialize a new User instance."""
        self.id = user_id
        self.pos = pos
        self.associated_ap = associated_ap
        self.application = None
        self.measured_bw = 0.0
        self.measured_delay = 0.0
        self.associated_app = None
        
print("[DEBUG 10] Entering function: assign_application")
def assign_application(self, application):
        """
        Assigns an application to the user and updates related attributes.
        
        Args:
            application (Application): The application to be assigned to the user.
        """
        self.application = application
        self.associated_app = application.name
        self.measured_bw = application.bandwidth
        self.measured_delay = application.latency
        
        class CNF:
print("[DEBUG 11] Exiting function: assign_application")
    """
    Represents a Cloud-Native Function (CNF) or a service component in the network.
    
    Attributes:
        name (str): The name of the CNF.
        cpu (float): CPU requirement for the CNF (e.g., in GHz).
        memory (float): Memory requirement for the CNF (e.g., in GB).
        storage (float): Storage requirement for the CNF (e.g., in GB).
        type (str): The type of CNF (e.g., 'Network', 'Analytics').
    """
print("[DEBUG 12] Entering function: __init__")
def __init__(self, name, cpu, memory, storage, type=None):
        """Initialize a new CNF instance."""
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.type = type
        
        class Application:
print("[DEBUG 13] Exiting function: __init__")
    """
    Represents an application consisting of one or more CNFs in the network.
    
    Attributes:
        name (str): The name of the application.
        bandwidth (float): The bandwidth required by the application (e.g., in Mbps).
        latency (float): The latency requirements of the application (e.g., in ms).
        device_density (int): The density of devices utilizing the application (e.g., devices per square km).
        source (str): The source or origin of the application requirements or data.
        sfc (list): The Service Function Chain, representing the sequence of CNFs required by the application.
        users (list): The users that are using this application.
        cnfs (list): The CNFs that make up this application.
    """
print("[DEBUG 14] Entering function: __init__")
def __init__(self, name, bandwidth, latency, device_density, source, sfc):
        """Initialize a new Application instance."""
        self.name = name
        self.bandwidth = bandwidth
        self.latency = latency
        self.device_density = device_density
        self.source = source
        self.sfc = sfc
        self.users = []
        self.cnfs = []
        
print("[DEBUG 15] Entering function: add_user")
def add_user(self, user):
        """
        Adds a user to this application's user list and assigns this application to the user.
        
        Args:
            user (User): The user to add and assign the application to.
        """
        self.users.append(user)
        user.assign_application(self)
        
print("[DEBUG 16] Entering function: add_cnf")
def add_cnf(self, cnf):
        """
        Adds a Cloud-Native Function (CNF) to this application.
        
        Args:
            cnf (CNF): The CNF to add to the application.
        """
        self.cnfs.append(cnf)
        
        
# Imported network_functions.py
print("[DEBUG 17] Exiting function: add_cnf")
# This is network_functions.py
# This file contains helper functions for parsing network data from XML and manipulating network structures using NetworkX.

import networkx as nx
import pandas as pd
import numpy as np
import math
from scipy.spatial.distance import euclidean
import random
import json
from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as plt
import xml.dom.minidom as dom
from network_classes import *
from collections import defaultdict


############ READ XML FUNCTIONS #########
print("[DEBUG 18] Entering function: read_nodes")
def read_nodes(nodelist):
print("[DEBUG 19] Exiting function: read_nodes")
    """
    Parses XML node elements into Node class instances.
    
    Args:
        nodelist (xml.dom.minidom.NodeList): List of node elements from XML.
        
    Returns:
        dict: Dictionary of node IDs mapped to Node instances.
    """
    nodes = {}
    for i, node in enumerate(nodelist):
        node_id = node.getAttribute("id")
        x_cor = float(node.getElementsByTagName('x')[0].firstChild.data)
        y_cor = float(node.getElementsByTagName('y')[0].firstChild.data)
        nodes[node_id] = Node(node_id, x_cor, y_cor)
    return nodes
    
print("[DEBUG 20] Entering function: read_links")
def read_links(linklist):
print("[DEBUG 21] Exiting function: read_links")
    """
    Parses XML link elements into Link class instances.
    
    Args:
        linklist (xml.dom.minidom.NodeList): List of link elements from XML.
        
    Returns:
        dict: Dictionary of link IDs mapped to Link instances.
    """
    links = {}
    for link in linklist:
        link_id = link.getAttribute("id")
        source = link.getElementsByTagName("source")[0].firstChild.data
        target = link.getElementsByTagName("target")[0].firstChild.data
        capacity = float(link.getElementsByTagName("capacity")[0].firstChild.data)
        cost = float(link.getElementsByTagName("cost")[0].firstChild.data)
        links[link_id] = Link(link_id, source, target, capacity, cost)
    return links
    
print("[DEBUG 22] Entering function: read_demands")
def read_demands(demandlist):
print("[DEBUG 23] Exiting function: read_demands")
    """
    Parses XML demand elements into Demand class instances.
    
    Args:
        demandlist (xml.dom.minidom.NodeList): List of demand elements from XML.
        
    Returns:
        dict: Dictionary of demand IDs mapped to Demand instances.
    """
    demands = {}
    for demand in demandlist:
        demand_id = demand.getAttribute("id")
        source = demand.getElementsByTagName("source")[0].firstChild.data
        destination = demand.getElementsByTagName("target")[0].firstChild.data
        demandValue = float(demand.getElementsByTagName("demandValue")[0].firstChild.data)
        demands[demand_id] = Demand(demand_id, source, destination, demandValue)
    return demands
    
print("[DEBUG 24] Entering function: read_XMLnetwork")
def read_XMLnetwork(filename):
print("[DEBUG 25] Exiting function: read_XMLnetwork")
    """
    Reads network configuration from an XML file and parses nodes, links, and demands.
    
    Args:
        filename (str): Path to the XML file containing network data.
        
    Returns:
        tuple: Contains three elements (nodes, links, demands) each represented as dictionaries.
    """
    Read_Data = dom.parse(filename)
    nodes = read_nodes(Read_Data.getElementsByTagName("node"))
    links = read_links(Read_Data.getElementsByTagName("link"))
    demands = read_demands(Read_Data.getElementsByTagName("demand"))
    return nodes, links, demands
    
    
############ NETWORKX GRAPH FUNCTIONS #########


print("[DEBUG 26] Entering function: calculate_distance")
def calculate_distance(x1, y1, x2, y2):
print("[DEBUG 27] Exiting function: calculate_distance")
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    
print("[DEBUG 28] Entering function: populate_network")
def populate_network(G, nodes, links, medium='fiber'):
print("[DEBUG 29] Exiting function: populate_network")
    """
    Populates a NetworkX graph with nodes and links based on provided dictionaries.
    Calculates and sets the propagation delay for each link based on the specified medium.
    
    Args:
        G (networkx.Graph): The graph to populate.
        nodes (dict): Dictionary of nodes.
        links (dict): Dictionary of links, which could be instances of Link or dictionaries.
        medium (str): Default communication medium for the network.
    """
    # Define propagation speeds for different media (in km/ms)
    propagation_speeds = {
        'fiber': 200,         # Fiber optic
        'ethernet': 200,      # Copper Ethernet
        'wifi': 300,          # Wi-Fi
        '5g': 300,            # 5G
        'lora': 300,          # LoRa (speed of light, though low data rate)
        'p2p_microwave': 300  # Point-to-point microwave
    }
    
    for node_id, node in nodes.items():
        G.add_node(node_id, pos=(node.x, node.y))
        
    for link_id, link in links.items():
        # Check if link is a dictionary or a Link object and access attributes accordingly
        if isinstance(link, dict):  # if the link is provided as a dictionary
            source, target = link['source'], link['target']
            capacity, cost = link['capacity'], link['cost']
            link_medium = link.get('medium', medium)  # Use specified medium or default
        else:  # if the link is a Link object
            source, target = link.source, link.target
            capacity, cost = link.capacity, link.cost
            link_medium = getattr(link, 'medium', medium)  # Use specified medium or default
            
        source_pos = G.nodes[source]['pos']
        target_pos = G.nodes[target]['pos']
        distance = calculate_distance(*source_pos, *target_pos)  # Unpacking coordinates
        speed = propagation_speeds.get(link_medium, 200)  # Use medium-specific speed
        latency = distance / speed  # Calculate latency based on distance and speed
        
        # Add the edge with calculated latency and other attributes
        G.add_edge(source, target, capacity=capacity, cost=cost, latency=latency, medium=link_medium)
        
        
        
        
#def draw_network_graph(G):
    """
    Draws the network graph using NetworkX and Matplotlib.
    
    Args:
        G (networkx.Graph): The graph to draw.
    """
    pos = nx.get_node_attributes(G, 'pos')
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10)
    plt.title('Network Topology')
    plt.show()
    
print("[DEBUG 30] Entering function: print_link_attributes")
def print_link_attributes(G):
print("[DEBUG 31] Exiting function: print_link_attributes")
    """
    Prints the attributes of each link in the network graph, including the latency
    which represents the propagation delay.
    
    Args:
        G (networkx.Graph): The graph containing the links.
    """
    link_table = PrettyTable()
    link_table.field_names = ["Edge", "Capacity (Mbps)", "Cost", "Propagation Delay (ms)", "Medium"]
    for (u, v, attrs) in G.edges(data=True):
        capacity = attrs['capacity']
        cost = attrs['cost']
        delay = attrs.get('latency', 'N/A')
        medium = attrs.get('medium', 'Not defined')
        link_table.add_row([f"{u} to {v}", capacity, cost, delay, medium])
    print("Graph Edges and their Attributes:")
    print(link_table)
    
print("[DEBUG 32] Entering function: print_node_attributes")
def print_node_attributes(G):
print("[DEBUG 33] Exiting function: print_node_attributes")
    """
    Prints the attributes of each node in the network graph.
    
    Args:
        G (networkx.Graph): The graph containing the nodes.
    """
    node_table = PrettyTable()
    node_table.field_names = ["Node", "x-coordinate", "y-coordinate", "Medium"]
    for node, attrs in G.nodes(data=True):
        x, y = attrs['pos']
        medium = attrs.get('medium', 'Not defined')
        node_table.add_row([node, x, y, medium])
    print("Graph Nodes and their Attributes:")
    print(node_table)
    
print("[DEBUG 34] Entering function: measure_network_stats")
def measure_network_stats(G):
print("[DEBUG 35] Exiting function: measure_network_stats")
    # Initialize PrettyTable
    table = PrettyTable()
    table.field_names = ["Metric", "Value", "Typical Range", "Interpretation"]
    
    # Network Density
    density = nx.density(G)
    table.add_row(["Density", f"{density:.4f}", "0 to 1", 
                "Higher values indicate a more connected network."])
                
    # Average Shortest Path Length
    if nx.is_connected(G):
        avg_shortest_path_length = nx.average_shortest_path_length(G)
    else:
        avg_shortest_path_length = np.mean([nx.average_shortest_path_length(G.subgraph(c)) for c in nx.connected_components(G) if len(c) > 1])
    table.add_row(["Average Shortest Path Length", f"{avg_shortest_path_length:.4f}", "Varies", 
                "Smaller values suggest higher efficiency in information flow."])
                
    # Average Clustering Coefficient
    avg_clustering_coefficient = nx.average_clustering(G)
    table.add_row(["Average Clustering Coefficient", f"{avg_clustering_coefficient:.4f}", "0 to 1", 
                "High values indicate tight-knit groups or cliques."])
                
    # Assortativity
    assortativity = nx.degree_assortativity_coefficient(G)
    table.add_row(["Assortativity", f"{assortativity:.4f}", "-1 to 1", 
                "Positive values: nodes connect to similar-degree nodes. Negative: high-degree nodes connect to low-degree ones."])
                
    # Network Modularity
    communities = list(nx.algorithms.community.label_propagation_communities(G))
    modularity = nx.algorithms.community.modularity(G, communities)
    table.add_row(["Network Modularity", f"{modularity:.4f}", "-0.5 to 1", 
                "Higher values indicate well-defined community structure."])
                
    # Network Efficiency
    efficiency = nx.global_efficiency(G)
    table.add_row(["Network Efficiency", f"{efficiency:.4f}", "0 to 1", 
                "Higher values indicate efficient communication across the network."])
                
    # Print the table
    print("Network Statistics and Metrics:")
    print(table)
    
    # PageRank
    pagerank_values = nx.pagerank(G)
    pagerank_table = PrettyTable()
    pagerank_table.field_names = ["Node", "PageRank", "Interpretation"]
    for node, rank in sorted(pagerank_values.items(), key=lambda item: item[1], reverse=True):
        pagerank_table.add_row([node, f"{rank:.4f}", 
                                "Higher values indicate more important or influential nodes."])
                                
    print("\nPageRank Weights:")
    print(pagerank_table)
    
    
################## USER FUNCTIONS ###################
print("[DEBUG 36] Entering function: find_nearest_ap")
def find_nearest_ap(G, user_pos):
print("[DEBUG 37] Exiting function: find_nearest_ap")
    """
    Find the nearest access point to a given user position.
    
    Args:
        G (networkx.Graph): The graph representing the network.
        user_pos (tuple): The (x, y) coordinates of the user.
        
    Returns:
        tuple: The ID and position (x, y) of the nearest access point, or (None, None) if no AP found.
    """
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
    
    
print("[DEBUG 38] Entering function: create_users")
def create_users(G, NoOfUsers, node_range=50):
print("[DEBUG 39] Exiting function: create_users")
    """
    Create a specified number of user nodes, each associated with the nearest access point.
    """
    G_users = nx.Graph()
    user_connections = []
    users = []
    
    user_count = 0
    while user_count < NoOfUsers:
        for node in G.nodes:
            if "Cloud" not in node:  # Skip cloud nodes
                x_cor, y_cor = G.nodes[node]['pos']
                randx = random.uniform(x_cor - node_range, x_cor + node_range)
                randy = random.uniform(y_cor - node_range, y_cor + node_range)
                user_pos = (randx, randy)
                nearest_ap, _ = find_nearest_ap(G, user_pos)
                if nearest_ap:
                    user_id = f"user_{user_count}"
                    user_instance = User(user_id, (randx, randy), nearest_ap)
                    users.append(user_instance)
                    G_users.add_node(user_id, pos=user_pos, user=user_instance)
                    #G_users.add_node(user_id, user=user_instance)  # Store the User instance
                    user_connections.append(((randx, randy), G.nodes[nearest_ap]['pos']))
                    user_count += 1
                if user_count >= NoOfUsers:
                    break
    return G_users, users, user_connections
    
    
    
    
    
################### SERVER FUNCTIONS ####################


print("[DEBUG 40] Entering function: associate_edge_devices")
def associate_edge_devices(G, edge_devices_filename, cloud_server_cost, edge_server_cost):
print("[DEBUG 41] Exiting function: associate_edge_devices")
    """
    Updates the attributes of the edge devices in the graph based on JSON data.
    
    Args:
        G (networkx.Graph): The graph representing the network.
        edge_devices_filename (str): The file path to the JSON data for edge devices.
        cloud_server_cost (float): The cost of the cloud server.
        edge_server_cost (float): The cost of the edge server.
    """
    with open(edge_devices_filename, "r") as file:
        edge_devices_data = json.load(file)
        
    for node in G.nodes():
        if "cloud" in node.lower():
            server = Server(
                "Huawei FusionServer Pro 2298 V5", 34253, "x86", 
                "75.6GHz", "3TB", "450TB", "Edge_Device_FusionServerPro2298",
                cloud_server_cost
            )
        else:
            server = Server(
                "Cisco HyperFlex HX220c Edge M5", 16408, "x86", 
                "34.8GHz", "1TB", "5TB", "Edge_Device_Cisco_HX220",
                edge_server_cost
            )
            
        # Update graph node attributes using the server object attributes
        G.nodes[node].update(vars(server))
        
        
print("[DEBUG 42] Entering function: print_edge_device_attributes")
def print_edge_device_attributes(G):
print("[DEBUG 43] Exiting function: print_edge_device_attributes")
    """
    Prints the attributes of all nodes in the graph, intended for edge devices, 
    using PrettyTable for formatting in a single table.
    
    Args:
        G (networkx.Graph): The graph representing the network with edge devices.
    """
    # Initialize PrettyTable and set the field names
    table = PrettyTable()
    # Assuming all nodes have the same attributes, use the first node to determine field names
    first_node_attrs = list(G.nodes(data=True))[0][1] if G.nodes else {}
    field_names = ['Node'] + [attr for attr in first_node_attrs]  # Add 'Node' as the first field name
    table.field_names = field_names
    
    # Fill the table with nodes' data
    for node, attrs in G.nodes(data=True):
        row = [node] + [attrs.get(attr, 'N/A') for attr in first_node_attrs]  # 'N/A' for missing attributes
        table.add_row(row)
        
    print(table)  # Print the table with all nodes and their attributes
    
    
    
print("[DEBUG 44] Entering function: associate_user_devices")
def associate_user_devices(G_users, traffic_json_path):
print("[DEBUG 45] Exiting function: associate_user_devices")
    print("Starting application association process...")
    
    # Load traffic data
    with open(traffic_json_path, "r") as file:
        traffic_data = json.load(file)["trafficStatistics"]
    print(f"Loaded {len(traffic_data)} traffic statistics.")
    
    # Assign application data to users
    for user_id in G_users.nodes:
        user_data = G_users.nodes[user_id]
        user = user_data.get('user')  # Ensure this is a User instance
        
        if user:  # Check if the user instance exists
            print(f"Assigning application to user: {user_id}")
            
            # Choose a random traffic statistic to assign to the user
            random_stat = random.choice(traffic_data)
            print(f"Selected application for {user_id}: {random_stat['application']}")
            
            # Compute average values if bandwidth and latency are lists
            avg_bandwidth = np.mean(random_stat["bandwidth"]) if isinstance(random_stat["bandwidth"], list) else random_stat["bandwidth"]
            avg_latency = np.mean(random_stat["latency"]) if isinstance(random_stat["latency"], list) else random_stat["latency"]
            
            # Update the user's data with the chosen application and its attributes
            application = Application(
                name=random_stat['application'],
                bandwidth=avg_bandwidth,
                latency=avg_latency,
                device_density=random_stat['deviceDensity'],
                source=random_stat['source'],
                sfc=[]  # Assuming this is filled elsewhere or not needed
            )
            user.assign_application(application)  # Assign the application to the user
            print(f"Assigned {application.name} to user {user_id} with bandwidth {avg_bandwidth} and latency {avg_latency}.")
        else:
            print(f"No user instance found for node: {user_id}")
            
    print("Application association process completed.")
    
    
    
    
    
    
print("[DEBUG 46] Entering function: print_user_device_attributes")
def print_user_device_attributes(G_users):
print("[DEBUG 47] Exiting function: print_user_device_attributes")
    table = PrettyTable()
    table.field_names = ["User", "Application", "Bandwidth (Mbps)", "Latency (ms)", "Device Density (/km^2)", "Source"]
    for user_id, data in G_users.nodes(data=True):
        user = data.get('user')  # Access the User instance
        if user and user.application:  # Check if user and user's application exist
            app = user.application  # Access the Application instance
            table.add_row([
                user_id, app.name, app.bandwidth, app.latency, 
                app.device_density, app.source
            ])
        else:
            table.add_row([user_id, "None", "N/A", "N/A", "N/A", "N/A"])
    print(table)
    
    
    
    
print("[DEBUG 48] Entering function: associate_app_with_containers")
def associate_app_with_containers(G_users, containers_json_path):
print("[DEBUG 49] Exiting function: associate_app_with_containers")
    """
    Assigns each application and its users to Containers, parsing from JSON file.
    """
    print("Starting container association process...")
    with open(containers_json_path, 'r') as f:
        containers_data = json.load(f)
        
    app_objects = {}  # Dictionary to store application objects
    app_to_users = defaultdict(list)  # Dictionary to map applications to users
    
    # Process each application in the container data
    for app_data in containers_data:
        app_name = app_data['application']
        # Check and add network and analytics functions
        cnfs = app_data.get('network_functions', []) + app_data.get('analytics_functions', [])
        
        # Initialize or update the Application instance
        if app_name not in app_objects:
            app_objects[app_name] = Application(
                name=app_name,
                bandwidth=app_data.get('bandwidth', 0),
                latency=app_data.get('latency', 0),
                device_density=app_data.get('device_density', 0),
                source="DefinedSource",  # Update as necessary
                sfc=app_data.get('sfc', [])
            )
            
        # Create and add CNFs for the application
        for cnf_data in cnfs:
            cnf = CNF(
                name=cnf_data['name'],
                cpu=float(cnf_data['cpu']),
                memory=float(cnf_data['memory']),
                storage=float(cnf_data['storage']),
                type='CNF'
            )
            app_objects[app_name].add_cnf(cnf)
            
    # Associate users from G_users to their applications
    for user_id, user_data in G_users.nodes(data=True):
        user = user_data['user']  # Extract the User instance
        if user and user.application:  # Check if user has an assigned application
            app_name = user.application.name
            if app_name in app_objects:
                app_objects[app_name].add_user(user)
                app_to_users[app_name].append(user_id)
                
    print("Container association process completed.")
    return dict(app_to_users), app_objects
    
print("[DEBUG 50] Entering function: print_applications_and_resources")
def print_applications_and_resources(app_objects):
print("[DEBUG 51] Exiting function: print_applications_and_resources")
    """
    Prints detailed information for each application and its associated resources.
    """
    for app_name, app in app_objects.items():
        print(f"Application Name: {app_name}")
        print(f"Associated Users: {', '.join([user.id for user in app.users])}")
        print(f"Service Function Chain: {', '.join(app.sfc)}")
        
        # Initialize PrettyTable for CNFs
        cnf_table = PrettyTable()
        cnf_table.field_names = ["CNF Name", "CPU (GHz)", "Memory (GB)", "Storage (GB)"]
        for cnf in app.cnfs:  # Follow the order defined in sfc
            cnf_table.add_row([cnf.name, cnf.cpu, cnf.memory, cnf.storage])
            
        print(cnf_table)
        print("---------------------------------------------------")
        
print("[DEBUG 52] Entering function: print_all_applications_and_resources")
def print_all_applications_and_resources(app_objects):
print("[DEBUG 53] Exiting function: print_all_applications_and_resources")
    # Initialize a PrettyTable instance for the applications
    app_table = PrettyTable()
    app_table.field_names = ["Application Name", "Associated Users", "Service Function Chain", "CNF Details"]
    
    # Iterate through each application and its details
    for app_name, app in app_objects.items():
        # Convert list of users to string
        users_str = ', '.join(user.id for user in app.users)
        
        # Convert list of CNFs to string
        cnf_details = "\n".join(f"{cnf.name}: CPU={cnf.cpu} GHz, Memory={cnf.memory} GB, Storage={cnf.storage} GB" for cnf in app.cnfs)
        
        # Convert list of CNFs in the service function chain to string
        sfc_str = ' -> '.join(cnf.name for cnf in app.cnfs)
        
        # Add the application details to the table
        app_table.add_row([app_name, users_str, sfc_str, cnf_details])
        
    print(app_table)
    
    
# Now the main simulation from main.py
print("[DEBUG 54] Entering function: execute_simulation")
def execute_simulation():
print("[DEBUG 55] Exiting function: execute_simulation")

    # # Initialization 
    
    
    # ## Parameters
    # 
    
    
    #Parameters:
    NoOfUsers = 30
    cloud_server_cost = 1000 #($/per server/hour)
    edge_server_cost = 100   #($/per server/hour)
    propagation_delay_constant = 1.5  # in ms/km
    routing_cost = 0.09 #($/GB)
    device_json_path = 'file-moV9mH3DMnZfynRtSM5GNr2R'
    traffic_json_path = "file-RwL2uZx8B7pM6y22iTkRGU4t"  # Adjust path as necessary
    containers_json_path = 'file-y5bfjds89iU3H3yf4w9ukAWZ'
    
    network_name = 'file-VWmgftA2WqSmsrsP87YoFjD3'  # Update this to the correct path to your XML file
    
    
    
    # # Class Definition
    
    
    
    nodes, links, demands = read_XMLnetwork(network_name)
    
    G = nx.Graph()
    # Populate the network, specifying '5g' as the default medium
    #Options include 'fiber', 'ethernet','wifi', '5g', 'lora', and 'p2p_microwave'
    populate_network(G, nodes, links, medium='5g')
    
    
    # Draw the graph
#    draw_network_graph(G)

    #Print node and link attributes
    print_node_attributes(G)
    print_link_attributes(G)
    measure_network_stats(G)
    
    
    
    # ## Generate Users
    # Here we will generate users
    # 
    # Generate Users: Randomly distrubuted users generated with uniform random distrubution of (x,y) corrdinates around the graph G that represents infrastrcuture. 
    # 
    # Allow options (ex. User_Spread).
    
    
    # Specify the number of users you want to generate
    # Create the users and their connections
    G_users, users, user_connections = create_users(G, NoOfUsers)
    
    # Draw the network and user graphs
    pos_G = nx.get_node_attributes(G, 'pos')
    pos_G_users = nx.get_node_attributes(G_users, 'pos')
    
    # Draw network nodes
    nx.draw(G, pos_G, with_labels=True, node_size=300, style="solid", node_color="blue")
    # Draw user nodes
    nx.draw(G_users, pos_G_users, with_labels=False, node_size=100, style="dashed", node_color="red", alpha=0.5)
    # Draw connections between users and their nearest APs
    for user_pos, ap_pos in user_connections:
        plt.plot([user_pos[0], ap_pos[0]], [user_pos[1], ap_pos[1]], color="green", linestyle="dashed")
        
    plt.show()
    
    
    
    # ## Assign Server Properties to each node in a uniform manner
    # 
    
    
    
        # Call the function with the JSON file path
    associate_edge_devices(G, device_json_path, cloud_server_cost, edge_server_cost)
    
    print_edge_device_attributes(G)
    
    
    # ## Assign Applications to users randomly to generate demand:
    # 
    # 
    
    
    #associate_user_devices(G_users, traffic_json_path)
    #print_user_device_attributes(G_users)
    
    
    
    associate_user_devices(G_users, traffic_json_path)
    
    
    print(f"Total users: {len(G_users.nodes())}")
    print_user_device_attributes(G_users)
    
    
    
    # ## Assign each application and its users to Containers (network_functions + analytics_functions)
    
    
    # Usage
    
    app_to_users, app_objects = associate_app_with_containers(G_users, containers_json_path)
    
    
    #print_applications_and_resources(app_objects)
    
    # After associating applications with containers
    print_all_applications_and_resources(app_objects)
    
    
    
    # # Placement
    
    
    # ## Random Microservice Placement + Routing
    
    
    from collections import defaultdict
    import random
    import networkx as nx
    
    # Initialize data structures to hold server and link states
    server_utilization_random = defaultdict(lambda: {'cpu': 0.0, 'memory': 0.0, 'storage': 0.0})
    link_utilization_random = defaultdict(float)
    accepted_users_count_random = 0
    rejected_users_count_random = 0
    total_routing_cost_random = 0.0
    link_cost_random = defaultdict(float)  # New dictionary to store the cost of each link
    total_propagation_delay_random = 0.0  # Initialize variable to hold total propagation delay
    # Initialize additional counters
    total_edge_servers_used_random = 0
    total_cloud_servers_used_random = 0
    total_cost_random = 0
    
    
    
    
    # Function to convert string capacity to float (e.g., '3TB' to 3000.0)
print("[DEBUG 56] Entering function: convert_capacity_to_float")
def convert_capacity_to_float(capacity_str):
        if 'GHz' in capacity_str:
            return float(capacity_str.replace('GHz', ''))
        elif 'x' in capacity_str:
            # Assuming the format is 'cores x speed' and you want total GHz
            cores, speed = capacity_str.split('x')
            return float(cores) * float(speed)
        elif 'TB' in capacity_str:
            return float(capacity_str.replace('TB', '')) * 1000  # Convert TB to GB
        else:
            return float(capacity_str)
            
            
    # Function to find a path that can handle the given bandwidth
print("[DEBUG 57] Entering function: find_feasible_path")
def find_feasible_path(G, source, target, bandwidth):
        for path in nx.all_simple_paths(G, source=source, target=target, cutoff=10):  # cutoff is optional, for performance
            can_use_path = True
            for i in range(len(path) - 1):
                link = (path[i], path[i + 1])
                link_capacity = G[path[i]][path[i + 1]]['capacity']  # Assuming capacity is in Mbps
                if link_utilization_random[link] + bandwidth > link_capacity:
                    can_use_path = False
                    break
            if can_use_path:
                return path
        return None
        
        
    accepted_users_count_random = 0
    rejected_users_count_random = 0
    
    # Random Microservice Placement
    for app_name, users in app_to_users.items():
        # Select a random server (node) for this application
        server = random.choice(list(G.nodes()))
        
        # Get the total resource requirements for this application
        container_list = [c for c in containers_data['Containers'] if c['application'] == app_name]
        if container_list:
            containers = container_list[0]
        else:
            print(f"No containers found for the application {app_name}")
            continue  # or handle this case appropriately
            
        total_cpu = sum(float(c['cpu']) for c in containers['vnfs'] + containers['microservices'])
        total_mem = sum(float(c['memory']) for c in containers['vnfs'] + containers['microservices'])
        total_storage = sum(float(c['storage']) for c in containers['vnfs'] + containers['microservices'])
        
        # Check server capacity and update server utilization
        server_capacity = G.nodes[server]
        if server_utilization_random[server]['cpu'] + total_cpu <= convert_capacity_to_float(server_capacity['cpu']) and \
            server_utilization_random[server]['memory'] + total_mem <= convert_capacity_to_float(server_capacity['memory']) and \
            server_utilization_random[server]['storage'] + total_storage <= convert_capacity_to_float(server_capacity['storage']):
            server_utilization_random[server]['cpu'] += total_cpu
            server_utilization_random[server]['memory'] += total_mem
            server_utilization_random[server]['storage'] += total_storage
            # Check if the server is an edge or cloud server and update the counter
            if "cloud" in server.lower():
                total_cloud_servers_used_random += 1
            else:
                total_edge_servers_used_random += 1
        else:
            print(f"Server capacity exceeded for server {server}")
            continue
            
        # Routing and link utilization
        for user in users:
            source_node = user_to_node_map[user]
            bandwidth = G_users.nodes[user]['bandwidth']
            path = find_feasible_path(G, source=source_node, target=server, bandwidth=bandwidth)
            
            if path:
                # Update link utilization and total routing cost along this path
                # for i in range(len(path) - 1):
                #     link = (path[i], path[i + 1])
                #     link_utilization_random[link] += bandwidth
                #     total_routing_cost_random += G[path[i]][path[i + 1]]['cost']
                #     accepted_users_count_random += 1
                # Update link utilization and total routing cost along this path
                user_propagation_delay = 0.0  # Initialize the user's total propagation delay to zero
                for i in range(len(path) - 1):
                    link = (path[i], path[i + 1])
                    link_utilization_random[link] += bandwidth
                    link_cost = bandwidth * 1e-3 * routing_cost
                    #link_cost = bandwidth * 1e-3 * G[path[i]][path[i + 1]]['cost']  # bandwidth in Gbps * cost ($/Gb)
                    link_cost_random[link] += link_cost  # Accumulate cost for this link
                    #total_routing_cost_random += G[path[i]][path[i + 1]]['cost']
                    total_routing_cost_random += link_cost  # Update the total routing cost
                    
                    # Add up the propagation delay for the current link to the user's total
                    user_propagation_delay += propagation_delays.get(link, 0)
                    accepted_users_count_random += 1
                # Add this user's propagation delay to the total
                total_propagation_delay_random += user_propagation_delay
            else:
                print(f"Could not find feasible path for user {user}")
                rejected_users_count_random += 1
                
    # Print server and link utilization
    # print("Server Utilization:")
    # for server, util in server_utilization_random.items():
    #     print(f"Server {server}: CPU = {util['cpu']} GHz, Memory = {util['memory']} GB, Storage = {util['storage']} GB")
    
    # print("\nLink Utilization:")
    # for link, bandwidth in link_utilization_random.items():
    #     print(f"Link {link}: {bandwidth} Mbps")
    
    # Print total routing cost
    print(f"\nTotal Routing Cost: {total_routing_cost_random}")
    
    #Print total accepted users
    print(f"\nTotal Accepted Users: {accepted_users_count_random}")
    accepted_percentage_random = accepted_users_count_random/NoOfUsers*100
    print(f"\nPercentage of Accepted Users: {accepted_percentage_random}%")
    
    
    #Print total rejected users
    print(f"\nTotal Rejected Users: {rejected_users_count_random}")
    rejected_percentage_random = rejected_users_count_random/NoOfUsers*100
    print(f"\nPercentage of Rejected Users: {rejected_percentage_random}%")
    
    
print("[DEBUG 58] Entering function: print_total_propagation_delay")
def print_total_propagation_delay():
        print(f"\nTotal Propagation Delay: {total_propagation_delay_random} ms")
        
    print_total_propagation_delay()
    
    # Additional print statements for the counters
    print(f"\nTotal Edge Servers Used: {total_edge_servers_used_random}")
    print(f"\nTotal Cloud Servers Used: {total_cloud_servers_used_random}")
    
    total_cost_random = total_routing_cost_random + total_edge_servers_used_random*edge_server_cost + total_cloud_servers_used_random*cloud_server_cost
    
    print(f"\nTotal cost: {total_cost_random}")
    
    
    
    # ### Ploting Random Microservice Placement
    
    
    import matplotlib.pyplot as plt
    import numpy as np
    
    
    # Server Utilization Bar Graph
    servers = list(server_utilization_random.keys())
    cpu_util = [server_utilization_random[s]['cpu'] for s in servers]
    mem_util = [server_utilization_random[s]['memory'] for s in servers]
    storage_util = [server_utilization_random[s]['storage'] for s in servers]
    
    barWidth = 0.25
    r1 = np.arange(len(cpu_util))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    
    plt.figure(figsize=(10, 6))
    plt.bar(r1, cpu_util, color='b', width=barWidth, edgecolor='grey', label='CPU (GHz)')
    plt.bar(r2, mem_util, color='c', width=barWidth, edgecolor='grey', label='Memory (GB)')
    plt.bar(r3, storage_util, color='m', width=barWidth, edgecolor='grey', label='Storage (GB)')
    
    plt.xlabel('Servers', fontweight='bold')
    plt.ylabel('Utilization')
    plt.title('Server Utilization')
    plt.xticks([r + barWidth for r in range(len(cpu_util))], servers)
    
    plt.legend()
    plt.show()
    
    #**********************************************************************************************************************
    
    # Link Utilization Bar Graph
    links = list(link_utilization_random.keys())
    bandwidth_util = [link_utilization_random[l] for l in links]
    link_names = [f"{l[0]}-{l[1]}" for l in links]
    
    plt.figure(figsize=(10, 6))
    plt.bar(link_names, bandwidth_util, color='r', edgecolor='grey')
    
    plt.xlabel('Links')
    plt.ylabel('Bandwidth (Mbps)')
    plt.title('Link Utilization')
    plt.xticks(rotation=45, ha='right')
    plt.show()
    
    
    #**********************************************************************************************************************
    
    # Create a new figure for Accepted and Rejected Users
    y_max = 100  # Adjust this value as needed
    
    # Create a new figure for Accepted and Rejected Users
    plt.figure(figsize=(10, 6))
    
    # Bar positions for Accepted and Rejected Users
    r4 = [x + barWidth for x in r3]
    
    user_percentages = [accepted_percentage_random, rejected_percentage_random]
    user_labels = ['Accepted Users', 'Rejected Users']
    
    # Set the bar positions at the center of the ticks
    bar_positions = [r + barWidth / 2 for r in r4[:2]]
    
    plt.bar(bar_positions, user_percentages, color=['g', 'r'], width=barWidth, edgecolor='grey')
    plt.xlabel('User Status')
    plt.ylabel('Percentage (%)')
    plt.title('Percentage of Accepted vs. Rejected Users')
    
    # Set the x-axis ticks at the center of the bars
    plt.xticks(bar_positions, user_labels)
    
    # Set the y-axis limit slightly above 100%
    plt.ylim(0, y_max)
    
    plt.show()
    
    
    # ## Placement using Page Rank in Descending page rank order
    # 
    
    
    from collections import defaultdict
    import random
    import networkx as nx
    import pandas as pd
    
    # Initialize data structures
    server_utilization_pagerank = defaultdict(lambda: {'cpu': 0.0, 'memory': 0.0, 'storage': 0.0})
    link_utilization_pagerank = defaultdict(float)
    total_routing_cost_pagerank = 0.0
    total_propagation_delay_pagerank = 0.0
    accepted_users_count_pagerank = 0
    rejected_users_count_pagerank = 0
    
    total_edge_servers_used_pagerank = 0
    total_cloud_servers_used_pagerank = 0
    total_cost_pagerank = 0.0
    used_edge_servers = set()
    used_cloud_servers = set()
    
    
    # Page Rank Weights
    # Replace this with your actual PageRank data
    pagerank_df = PageRank.compute_pagerank(G)
    sorted_pagerank = pagerank_df.sort_values(by='value', ascending=False)
    
    # Function to calculate a composite score for server selection
print("[DEBUG 59] Entering function: server_score")
def server_score(pagerank, server_utilization):
        return pagerank - 0.01 * (server_utilization['cpu'] + server_utilization['memory'] + server_utilization['storage'])
        
        
        
    # Function to convert string capacity to float (e.g., '3TB' to 3000.0)
print("[DEBUG 60] Entering function: convert_capacity_to_float")
def convert_capacity_to_float(capacity_str):
        if 'GHz' in capacity_str:
            return float(capacity_str.replace('GHz', ''))
        elif 'TB' in capacity_str:
            return float(capacity_str.replace('TB', '')) * 1000  # Convert TB to GB
        else:
            return float(capacity_str)
            
    # Function to find a path that can handle the given bandwidth
print("[DEBUG 61] Entering function: find_feasible_path")
def find_feasible_path(G, source, target, bandwidth):
        for path in nx.all_simple_paths(G, source=source, target=target, cutoff=50):  # cutoff is optional, for performance
            can_use_path = True
            for i in range(len(path) - 1):
                link = (path[i], path[i + 1])
                link_capacity = G[path[i]][path[i + 1]]['capacity']  # Assuming capacity is in Mbps
                if link_utilization_pagerank[link] + bandwidth > link_capacity:
                    can_use_path = False
                    break
            if can_use_path:
                return path
        return None
        
    # Microservice Placement using PageRank
    for app_name, users in app_to_users.items():
    
        # Sort servers by PageRank and current utilization
        #sorted_pagerank['server_score'] = sorted_pagerank.apply(lambda row: server_score(row['value'], server_utilization_pagerank[row['name']]), axis=1)
        #sorted_servers = sorted_pagerank.sort_values(by='server_score', ascending=False)['name'].tolist()
        
        #for server in sorted_servers:
        for _, row in sorted_pagerank.iterrows():
            server = row['name']
            
            # Get the total resource requirements for this application
            container_list = [c for c in containers_data['Containers'] if c['application'] == app_name]
            if container_list:
                containers = container_list[0]
            else:
                print(f"No containers found for the application {app_name}")
                break
                
            total_cpu = sum(float(c['cpu']) for c in containers['vnfs'] + containers['microservices'])
            total_mem = sum(float(c['memory']) for c in containers['vnfs'] + containers['microservices'])
            total_storage = sum(float(c['storage']) for c in containers['vnfs'] + containers['microservices'])
            
            # Check server capacity
            server_capacity = G.nodes[server]
            if server_utilization_pagerank[server]['cpu'] + total_cpu <= convert_capacity_to_float(server_capacity['cpu']) and \
            server_utilization_pagerank[server]['memory'] + total_mem <= convert_capacity_to_float(server_capacity['memory']) and \
            server_utilization_pagerank[server]['storage'] + total_storage <= convert_capacity_to_float(server_capacity['storage']):
            
                # Update server utilization
                server_utilization_pagerank[server]['cpu'] += total_cpu
                server_utilization_pagerank[server]['memory'] += total_mem
                server_utilization_pagerank[server]['storage'] += total_storage
                
                # Update the total number of edge/cloud servers used
                if "cloud" in server.lower():
                    used_cloud_servers.add(server)
                else:
                used_edge_servers.add(server)
                break
            else:
                continue  # Move to next highest PageRank server
                
        # Routing and link utilization
        for user in users:
            source_node = user_to_node_map[user]
            bandwidth = G_users.nodes[user]['bandwidth']
            path = find_feasible_path(G, source=source_node, target=server, bandwidth=bandwidth)
            
            if path:
                user_propagation_delay = 0.0  # Initialize the user's total propagation delay to zero
                for i in range(len(path) - 1):
                    link = (path[i], path[i + 1])
                    link_utilization_pagerank[link] += bandwidth
                    link_cost = bandwidth * 1e-3 * routing_cost
                    #total_routing_cost_pagerank += G[path[i]][path[i + 1]]['cost']
                    total_routing_cost_pagerank += link_cost
                    user_propagation_delay += propagation_delays.get(link, 0)  # Assuming you have a propagation_delays dict
                    
                # Add this user's propagation delay to the total
                total_propagation_delay_pagerank += user_propagation_delay
                accepted_users_count_pagerank += 1
            else:
                print(f"Could not find feasible path for user {user}")
                rejected_users_count_pagerank += 1
                
    # Print server and link utilization
    print("Server Utilization:")
    for server, util in server_utilization_pagerank.items():
        print(f"Server {server}: CPU = {util['cpu']} GHz, Memory = {util['memory']} GB, Storage = {util['storage']} GB")
        
    print("\nLink Utilization:")
    for link, bandwidth in link_utilization_pagerank.items():
        continue
        #print(f"Link {link}: {bandwidth} Mbps")
        
    # Print total routing cost
    print(f"\nTotal Routing Cost: {total_routing_cost_pagerank}")
    
    
    # Print total propagation delay
    print(f"\nTotal Propagation Delay: {total_propagation_delay_pagerank} ms")
    
    # Print total accepted and rejected users
    print(f"\nTotal Accepted Users: {accepted_users_count_pagerank}")
    accepted_percentage_pagerank = accepted_users_count_pagerank / NoOfUsers * 100
    print(f"\nPercentage of Accepted Users: {accepted_percentage_pagerank}%")
    
    print(f"\nTotal Rejected Users: {rejected_users_count_pagerank}")
    rejected_percentage_pagerank = rejected_users_count_pagerank / NoOfUsers * 100
    print(f"\nPercentage of Rejected Users: {rejected_percentage_pagerank}%")
    
    total_edge_servers_used_pagerank = len(used_edge_servers)
    total_cloud_servers_used_pagerank = len(used_cloud_servers)
    
    # Additional print statements for the counters
    print(f"\nTotal Edge Servers Used: {total_edge_servers_used_pagerank}")
    print(f"\nTotal Cloud Servers Used: {total_cloud_servers_used_pagerank}")
    
    total_cost_pagerank = total_routing_cost_pagerank + total_edge_servers_used_pagerank*edge_server_cost + total_cloud_servers_used_pagerank*cloud_server_cost
    print(f"\nTotal cost: {total_cost_pagerank}")
    
    
    
    
    
    
    
    
    # Debug Script: Print the state of all relevant variables for diagnostics
    
    # Ensure all necessary imports are present
    from collections import defaultdict
    import networkx as nx
    
    # Assuming the existence of variables and data structures from your context
    
    # Print app_to_users content
    print("Debug - app_to_users content:", app_to_users)
    
    
    # Print the graph G nodes and edges if needed
    print("\nGraph G Nodes and Edges:")
    print("Nodes:", G.nodes(data=True))
    print("Edges:", G.edges(data=True))
    
    # Print feasible paths (Assuming you have a way to collect these)
    # This part needs to be integrated with your path finding and processing logic
    # Here's an example placeholder for how you might structure this
    print("\nFeasible Paths:")
    # Assuming feasible_paths is a list of tuples (path, bandwidth)
    # You would need to modify your path finding to collect these
    feasible_paths = []  # Placeholder for where you would collect feasible paths
    for path, bandwidth in feasible_paths:
        print(f"Path: {path} with bandwidth {bandwidth} Mbps")
        
    # Print any other specific variables you're interested in
    # For example, capacities, apps, users, etc.
    # Example placeholder for server capacities
    print("\nServer Capacities:")
    # Assuming a dictionary or graph node attribute for server capacities
    for server in G.nodes():
        attrs = G.nodes[server]
        print(f"Server {server}: CPU = {attrs.get('cpu', 'N/A')}, Memory = {attrs.get('memory', 'N/A')}, Storage = {attrs.get('storage', 'N/A')}")
        
    # Add similar sections for any other variables or data structures you wish to debug
    
    
    
    
    import matplotlib.pyplot as plt
    import numpy as np
    
    # Assuming you have server_utilization, link_utilization, accepted_percentage, and rejected_percentage already defined
    
    # Server Utilization Bar Graph
    servers = list(server_utilization_pagerank.keys())
    cpu_util = [server_utilization_pagerank[s]['cpu'] for s in servers]
    mem_util = [server_utilization_pagerank[s]['memory'] for s in servers]
    storage_util = [server_utilization_pagerank[s]['storage'] for s in servers]
    
    barWidth = 0.25
    r1 = np.arange(len(cpu_util))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    
    plt.figure(figsize=(10, 6))
    plt.bar(r1, cpu_util, color='b', width=barWidth, edgecolor='grey', label='CPU (GHz)')
    plt.bar(r2, mem_util, color='c', width=barWidth, edgecolor='grey', label='Memory (GB)')
    plt.bar(r3, storage_util, color='m', width=barWidth, edgecolor='grey', label='Storage (GB)')
    
    plt.xlabel('Servers', fontweight='bold')
    plt.ylabel('Utilization')
    plt.title('Server Utilization')
    plt.xticks([r + barWidth for r in range(len(cpu_util))], servers)
    
    plt.legend()
    plt.show()
    
    # Link Utilization Bar Graph
    links = list(link_utilization_pagerank.keys())
    bandwidth_util = [link_utilization_pagerank[l] for l in links]
    link_names = [f"{l[0]}-{l[1]}" for l in links]
    
    plt.figure(figsize=(10, 6))
    plt.bar(link_names, bandwidth_util, color='r', edgecolor='grey')
    
    plt.xlabel('Links')
    plt.ylabel('Bandwidth (Mbps)')
    plt.title('Link Utilization')
    plt.xticks(rotation=45, ha='right')
    plt.show()
    
    # Accepted vs Rejected Users Bar Graph
    y_max = 100  # Adjust this value as needed
    
    plt.figure(figsize=(10, 6))
    
    user_percentages = [accepted_percentage_pagerank, rejected_percentage_pagerank]
    user_labels = ['Accepted Users', 'Rejected Users']
    
    bar_positions = np.arange(len(user_labels))
    
    plt.bar(bar_positions, user_percentages, color=['g', 'r'], edgecolor='grey')
    
    plt.xlabel('User Status')
    plt.ylabel('Percentage (%)')
    plt.title('Percentage of Accepted vs. Rejected Users')
    plt.xticks(bar_positions, user_labels)
    plt.ylim(0, y_max)
    
    plt.show()
    
    
    
    # ## Adaptive VNF Placement Algorithm
    # 
    # 1. *Determining Service Order Algorithm*: This algorithm takes several parameters like sets of users, SFCs, bandwidth requirements, and computational demands and times for CNFs. It calculates the urgency and criticality for each SFC and sorts them.
    # 2. *Placement Algorithm*: For each application in the sorted Service Order Queue, it tries to place the most critical VNF on the Central_Server. If that's not possible, it calculates a Candidate score for each node and sorts them to find the next best candidate.
    # 3. *Experimental Setup and Results*: You have graphs for the average number of servers used, SFC length, algorithm execution time, CPU utilization, and link utilization.
    
    
    from collections import defaultdict
    import random
    import networkx as nx
    
    # Initialize data structures to hold server and link states
    server_utilization_adaptive = defaultdict(lambda: {'cpu': 0.0, 'memory': 0.0, 'storage': 0.0})
    link_utilization_adaptive = defaultdict(float)
    link_cost_adaptive = defaultdict(float)
    total_routing_cost_adaptive = 0.0
    total_propagation_delay_adaptive = 0.0
    accepted_users_count_adaptive = 0
    rejected_users_count_adaptive = 0
    
    # Initialize additional counters
    total_edge_servers_used_adaptive = 0
    total_cloud_servers_used_adaptive = 0
    total_cost_adaptive = 0.0
    
print("[DEBUG 62] Entering function: convert_capacity_to_float")
def convert_capacity_to_float(capacity_str):
        if 'GHz' in capacity_str:
            return float(capacity_str.replace('GHz', ''))
        elif 'TB' in capacity_str:
            return float(capacity_str.replace('TB', '')) * 1000
        else:
            return float(capacity_str)
            
print("[DEBUG 63] Entering function: find_feasible_path")
def find_feasible_path(G, source, target, bandwidth):
        try:
            path = nx.shortest_path(G, source=source, target=target, weight='cost')
            can_use_path = all(
                link_utilization_adaptive[(path[i], path[i + 1])] + bandwidth <= G[path[i]][path[i + 1]]['capacity']
                for i in range(len(path) - 1)
            )
            if can_use_path:
                return path
        except nx.NetworkXNoPath:
            pass
        return None
        
print("[DEBUG 64] Entering function: compute_link_cost")
def compute_link_cost(G, path, bandwidth):
        cost = 0.0
        for i in range(len(path) - 1):
            link = (path[i], path[i + 1])
            cost += bandwidth * 1e-3 * routing_cost
            link_cost_adaptive[link] += cost
        return cost
        
    # ... (your existing code for populating G, G_users, app_to_users, user_to_node_map, containers_data, propagation_delays)
    
    for app_name, users in app_to_users.items():
        sorted_servers = sorted(G.nodes(), key=lambda x: server_utilization_adaptive[x]['cpu'])
        
        for server in sorted_servers:
            container_list = [c for c in containers_data['Containers'] if c['application'] == app_name]
            if not container_list:
                print(f"No containers found for the application {app_name}")
                break
                
            containers = container_list[0]
            total_cpu = sum(float(c['cpu']) for c in containers['vnfs'] + containers['microservices'])
            total_mem = sum(float(c['memory']) for c in containers['vnfs'] + containers['microservices'])
            total_storage = sum(float(c['storage']) for c in containers['vnfs'] + containers['microservices'])
            
            server_capacity = G.nodes[server]
            if all(
                server_utilization_adaptive[server][resource] + total <= convert_capacity_to_float(server_capacity[resource])
                for resource, total in [('cpu', total_cpu), ('memory', total_mem), ('storage', total_storage)]
            ):
                for resource, total in [('cpu', total_cpu), ('memory', total_mem), ('storage', total_storage)]:
                    server_utilization_adaptive[server][resource] += total
                    
                # Update the total number of edge/cloud servers used
                if "cloud" in server.lower():
                    total_cloud_servers_used_adaptive += 1
                else:
                    total_edge_servers_used_adaptive += 1
                    
                break
                
        for user in users:
            source_node = user_to_node_map[user]
            bandwidth = G_users.nodes[user]['bandwidth']
            path = find_feasible_path(G, source=source_node, target=server, bandwidth=bandwidth)
            
            if path:
                user_propagation_delay = 0.0
                path_cost = compute_link_cost(G, path, bandwidth)
                for i in range(len(path) - 1):
                    link = (path[i], path[i + 1])
                    link_utilization_adaptive[link] += bandwidth
                    total_routing_cost_adaptive += bandwidth * 1e-3 * routing_cost
                    user_propagation_delay += propagation_delays.get(link, 0)
                total_propagation_delay_adaptive += user_propagation_delay
                accepted_users_count_adaptive += 1
            else:
                print(f"Could not find feasible path for user {user}")
                rejected_users_count_adaptive += 1
                
    # Additional print statements for the counters
    print(f"\nTotal Edge Servers Used: {total_edge_servers_used_adaptive}")
    print(f"\nTotal Cloud Servers Used: {total_cloud_servers_used_adaptive}")
    
    total_cost_adaptive = total_routing_cost_adaptive + total_edge_servers_used_adaptive*edge_server_cost + total_cloud_servers_used_adaptive*cloud_server_cost
    print(f"\nTotal cost: {total_cost_adaptive} $")
    
    print("\nCost for Each Link:")
    for link, cost in link_cost_adaptive.items():
        print(f"Link {link}: {cost} $")
        
    print(f"\nTotal routing cost: {total_routing_cost_adaptive} $")
    print(f"\nTotal Propagation Delay: {total_propagation_delay_adaptive} ms")
    print(f"\nTotal Accepted Users: {accepted_users_count_adaptive}")
    
    
    
    # Adaptive Placement Plotting
    
    import matplotlib.pyplot as plt
    import numpy as np
    
    # Server Utilization Bar Graph
    servers = list(server_utilization_adaptive.keys())
    cpu_util = [server_utilization_adaptive[s]['cpu'] for s in servers]
    mem_util = [server_utilization_adaptive[s]['memory'] for s in servers]
    storage_util = [server_utilization_adaptive[s]['storage'] for s in servers]
    
    barWidth = 0.25
    r1 = np.arange(len(cpu_util))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    
    plt.figure(figsize=(10, 6))
    plt.bar(r1, cpu_util, color='b', width=barWidth, edgecolor='grey', label='CPU (GHz)')
    plt.bar(r2, mem_util, color='c', width=barWidth, edgecolor='grey', label='Memory (GB)')
    plt.bar(r3, storage_util, color='m', width=barWidth, edgecolor='grey', label='Storage (GB)')
    
    plt.xlabel('Servers', fontweight='bold')
    plt.ylabel('Utilization')
    plt.title('Server Utilization')
    plt.xticks([r + barWidth for r in range(len(cpu_util))], servers)
    
    plt.legend()
    plt.show()
    
    # Link Utilization Bar Graph
    links = list(link_utilization_adaptive.keys())
    bandwidth_util = [link_utilization_adaptive[l] for l in links]
    link_names = [f"{l[0]}-{l[1]}" for l in links]
    
    plt.figure(figsize=(10, 6))
    plt.bar(link_names, bandwidth_util, color='r', edgecolor='grey')
    
    plt.xlabel('Links')
    plt.ylabel('Bandwidth (Mbps)')
    plt.title('Link Utilization')
    plt.xticks(rotation=45, ha='right')
    plt.show()
    
    # Accepted vs Rejected Users Bar Graph
    y_max = 100  # Adjust this value as needed
    
    accepted_percentage_adaptive = (accepted_users_count_adaptive / NoOfUsers) * 100
    rejected_percentage_adaptive = (rejected_users_count_adaptive / NoOfUsers) * 100
    
    plt.figure(figsize=(10, 6))
    
    user_percentages = [accepted_percentage_adaptive, rejected_percentage_adaptive]
    user_labels = ['Accepted Users', 'Rejected Users']
    
    bar_positions = np.arange(len(user_labels))
    
    plt.bar(bar_positions, user_percentages, color=['g', 'r'], edgecolor='grey')
    
    plt.xlabel('User Status')
    plt.ylabel('Percentage (%)')
    plt.title('Percentage of Accepted vs. Rejected Users')
    plt.xticks(bar_positions, user_labels)
    plt.ylim(0, y_max)
    
    plt.show()
    
    
    
    # # Combined Plots for Random Placement, Page Rank Placement and Adaptive Placement Algorithms
    
    
    import matplotlib.pyplot as plt
    import numpy as np
    
    # Server Utilization Plot
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))
    
    # Assuming you have server_utilization_adaptive, server_utilization_pagerank, server_utilization_random
    server_labels = ['Random', 'PageRank', 'Adaptive']
    
    # CPU Utilization
    cpu_util = [
        np.mean([server_utilization_random[s]['cpu'] for s in server_utilization_random]),
        np.mean([server_utilization_pagerank[s]['cpu'] for s in server_utilization_pagerank]),
        np.mean([server_utilization_adaptive[s]['cpu'] for s in server_utilization_adaptive])
    ]
    
    # Memory Utilization
    mem_util = [
        np.mean([server_utilization_random[s]['memory'] for s in server_utilization_random]),
        np.mean([server_utilization_pagerank[s]['memory'] for s in server_utilization_pagerank]),
        np.mean([server_utilization_adaptive[s]['memory'] for s in server_utilization_adaptive])
    ]
    
    # Storage Utilization
    storage_util = [
        np.mean([server_utilization_random[s]['storage'] for s in server_utilization_random]),
        np.mean([server_utilization_pagerank[s]['storage'] for s in server_utilization_pagerank]),
        np.mean([server_utilization_adaptive[s]['storage'] for s in server_utilization_adaptive])
    ]
    
    barWidth = 0.25
    r1 = np.arange(len(cpu_util))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    #*********************************************************************************************************************************************
    # Plotting CPU Utilization
    axs[0].bar(r1, cpu_util, color='b', width=barWidth, edgecolor='grey', label='CPU (GHz)')
    axs[0].set_title('Average CPU Utilization')
    axs[0].set_xticks([r + barWidth for r in range(len(cpu_util))])
    axs[0].set_xticklabels(server_labels)
    axs[0].legend()
    #*********************************************************************************************************************************************
    # Plotting Memory Utilization
    axs[1].bar(r1, mem_util, color='c', width=barWidth, edgecolor='grey', label='Memory (GB)')
    axs[1].set_title('Average Memory Utilization')
    axs[1].set_xticks([r + barWidth for r in range(len(mem_util))])
    axs[1].set_xticklabels(server_labels)
    axs[1].legend()
    #*********************************************************************************************************************************************
    # Plotting Storage Utilization
    axs[2].bar(r1, storage_util, color='m', width=barWidth, edgecolor='grey', label='Storage (GB)')
    axs[2].set_title('Average Storage Utilization')
    axs[2].set_xticks([r + barWidth for r in range(len(storage_util))])
    axs[2].set_xticklabels(server_labels)
    axs[2].legend()
    
    plt.show()
    
    #*********************************************************************************************************************************************
    # Plotting Link Utilization
    plt.figure()
    avg_link_util = [
        np.mean(list(link_utilization_random.values())),
        np.mean(list(link_utilization_pagerank.values())),
        np.mean(list(link_utilization_adaptive.values()))
    ]
    
    plt.bar(server_labels, avg_link_util, color='r', edgecolor='grey')
    plt.title('Average Link Utilization')
    plt.xlabel('Algorithm')
    plt.ylabel('Bandwidth (Mbps)')
    plt.show()
    
    #*********************************************************************************************************************************************
    
    # Plotting % of Accepted Users
    plt.figure()
    accepted_users_percentage = [
        (accepted_users_count_random / (accepted_users_count_random + rejected_users_count_random)) * 100 if accepted_users_count_random + rejected_users_count_random > 0 else 0,
        (accepted_users_count_pagerank / (accepted_users_count_pagerank + rejected_users_count_pagerank)) * 100 if accepted_users_count_pagerank + rejected_users_count_pagerank > 0 else 0,
        (accepted_users_count_adaptive / (accepted_users_count_adaptive + rejected_users_count_adaptive)) * 100 if accepted_users_count_adaptive + rejected_users_count_adaptive > 0 else 0
    ]
    
    plt.bar(server_labels, accepted_users_percentage, color='g', edgecolor='grey')
    plt.title('Percentage of Accepted Users')
    plt.xlabel('Algorithm')
    plt.ylabel('Percentage (%)')
    plt.show()
    
    #*********************************************************************************************************************************************
    
    # Plotting % of Rejected Users
    plt.figure()
    rejected_users_percentage = [
        (rejected_users_count_random / (accepted_users_count_random + rejected_users_count_random)) * 100 if accepted_users_count_random + rejected_users_count_random > 0 else 0,
        (rejected_users_count_pagerank / (accepted_users_count_pagerank + rejected_users_count_pagerank)) * 100 if accepted_users_count_pagerank + rejected_users_count_pagerank > 0 else 0,
        (rejected_users_count_adaptive / (accepted_users_count_adaptive + rejected_users_count_adaptive)) * 100 if accepted_users_count_adaptive + rejected_users_count_adaptive > 0 else 0
    ]
    
    plt.bar(server_labels, rejected_users_percentage, color='g', edgecolor='grey')
    plt.title('Percentage of Rejected Users')
    plt.xlabel('Algorithm')
    plt.ylabel('Percentage (%)')
    plt.show()
    
    #*********************************************************************************************************************************************
    # New Plot for Total Propagation Delay
    plt.figure()
    total_propagation_delay_values = [
        total_propagation_delay_random,
        total_propagation_delay_pagerank,
        total_propagation_delay_adaptive
    ]
    
    plt.bar(server_labels, total_propagation_delay_values, color='orange', edgecolor='grey')
    plt.title('Total Propagation Delay')
    plt.xlabel('Algorithm')
    plt.ylabel('Delay (ms)')
    plt.show()
    
    
    #*********************************************************************************************************************************************
    
    # New Plot for Total Routing Cost
    plt.figure()
    total_routing_cost_values = [
        total_routing_cost_random,
        total_routing_cost_pagerank,
        total_routing_cost_adaptive
    ]
    
    fig, ax = plt.subplots()
    ax.bar(server_labels, total_routing_cost_values, color='purple', edgecolor='grey')
    
    plt.title('Total Routing Cost')
    plt.xlabel('Algorithm')
    plt.ylabel('Cost (USD)')
    plt.show()
    #*********************************************************************************************************************************************
    
    #Plot for total cost
    
    plt.figure()
    total_cost_values = [
        total_cost_random,
        total_cost_pagerank,
        total_cost_adaptive
    ]
    
    fig, ax = plt.subplots()
    ax.bar(server_labels, total_cost_values, color='purple', edgecolor='grey')
    
    plt.title('Total Cost')
    plt.xlabel('Algorithm')
    plt.ylabel('Cost (USD)')
    plt.show()
    
    #*********************************************************************************************************************************************
    
    # Data
    algorithms = ['Random', 'PageRank', 'Adaptive']
    edge_servers = [
        total_edge_servers_used_random,
        total_edge_servers_used_pagerank,
        total_edge_servers_used_adaptive
    ]
    cloud_servers = [
        total_cloud_servers_used_random,
        total_cloud_servers_used_pagerank,
        total_cloud_servers_used_adaptive
    ]
    
    # Set up the bar chart
    x = np.arange(len(algorithms))  # the label locations
    width = 0.35  # the width of the bars
    
    fig, ax = plt.subplots()
    
    rects1 = ax.bar(x - width/2, edge_servers, width, label='Edge Servers')
    rects2 = ax.bar(x + width/2, cloud_servers, width, label='Cloud Servers')
    
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('Algorithms')
    ax.set_title('Total Edge and Cloud Servers Used by Different Algorithms')
    ax.set_xticks(x)
    ax.set_xticklabels(algorithms)
    ax.legend()
    
    # Autolabel function to display the label on top of the bars
print("[DEBUG 65] Entering function: autolabel")
def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
                        
    autolabel(rects1)
    autolabel(rects2)
    
    plt.show()
    
    
    print("Edge Servers Used (Random): ", total_edge_servers_used_random)
    print("Cloud Servers Used (Random): ", total_cloud_servers_used_random)
    
    
    
    
    
    # # GAMS
    # 
    
    
    # ## GAMS Connection
    # 
    
    
    import subprocess
    
print("[DEBUG 66] Entering function: run_gams_model")
def run_gams_model(gams_path, model_file, log_option, output_gdx):
        """
        Run a GAMS model using Python.
        
        Parameters:
        gams_path (str): Full path to the GAMS executable.
        model_file (str): The GAMS model file to run.
        log_option (str): Log level option for GAMS.
        input_gdx (str): GDX file for input data.
        output_gdx (str): GDX file for output data.
        """
        
        # Construct the command to run the GAMS model
        command = f'"{gams_path}" {model_file} lo={log_option} gdx={output_gdx}'
        
        # Run the command and capture output
        try:
            completed_process = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("GAMS model executed successfully.")
            print(completed_process.stdout.decode())
            print(completed_process.stderr.decode())
        except subprocess.CalledProcessError as e:
            print("An error occurred in GAMS model execution.")
            print(e)
            print(e.stdout.decode())
            print(e.stderr.decode())
            
    # Path to your GAMS installation
    gams_path = 'C:\\GAMS\\win64\\24.9\\gams'
    
    # Your GAMS model file
    model_file = 'm2'
    
    # Define the path to your input GDX file
    input_gdx = 'Optimization_input.gdx'
    
    # Log option and output GDX file name
    log_option = '3'
    output_gdx = 'Optimization_output'
    
    # Run the GAMS model
    run_gams_model(gams_path, model_file, log_option, output_gdx)
    
    
    
    import os
    import gams
    from gams import GamsWorkspace
    
    # Define paths to your GAMS installation and GAMS model file
    gams_path = 'C:\\GAMS\\win64\\24.9\\gams.exe'
    model_file = 'm2.gms'
    input_gdx = 'data.gdx'
    output_gdx = 'Optimization_output.gdx'
    
    # Get the absolute path to the current directory
    current_directory = os.getcwd()
    
    # Construct the absolute path to the output GDX file
    output_gdx_absolute = os.path.join(current_directory, output_gdx)
    
    # Function to verify GDX contents
print("[DEBUG 67] Entering function: verify_gdx_contents")
def verify_gdx_contents(gdx_file_path):
        ws = gams.GamsWorkspace()
        db = ws.add_database_from_gdx(gdx_file_path)
        
        for symbol in db:
            print(f"Symbol: {symbol.name}, Type: {type(symbol).__name__}")
            if isinstance(symbol, gams.GamsSet):
                print("  Elements:")
                for record in symbol:
                    print(f"    {record.key(0)}")
            elif isinstance(symbol, gams.GamsParameter):
                print("  Values:")
                if len(symbol.domains) == 2:  # Check if the parameter has two-dimensional indices
                    for record in symbol:
                        print(f"    {record.keys[0]}-{record.keys[1]}: {record.value}")
                elif symbol.name == "Topology":  # Check if the parameter is 'Topology'
                    for record in symbol:
                        print(f"    {record.key(0)}-{record.keys[0]}: {record.value}")
                else:
                    try:
                        for record in symbol:
                            print(f"    {record.key(0)}: {record.value}")
                    except Exception as e:
                        print(f"    Error accessing values: {e}")
            elif isinstance(symbol, gams.GamsVariable):
                print("  Values:")
                try:
                    for record in symbol:
                        print(f"    {record.key}: {record.level}")
                except Exception as e:
                    print(f"    Error accessing levels: {e}")
            else:
                print("  Unknown type")
                
                
                
                
                
                
    # Verify the output GDX file contents
    verify_gdx_contents(output_gdx_absolute)
    
    
    
    import os
    import subprocess
    import networkx as nx
    from gams import GamsWorkspace
    
    # Define paths and settings
    gams_system_directory = 'C:\\GAMS\\win64\\24.9'
    gdx_file_path = 'data.gdx'
    output_gdx = 'Optimization_output.gdx'
    current_directory = os.getcwd()
    
    # Initialize GAMS workspace
    ws = GamsWorkspace(system_directory=gams_system_directory, working_directory=current_directory)
    
    # Verify GDX contents function
print("[DEBUG 68] Entering function: verify_gdx_contents")
def verify_gdx_contents(gdx_file_path):
        db = ws.add_database_from_gdx(gdx_file_path)
        
        for symbol in db:
            print(f"Symbol: {symbol.name}, Type: {type(symbol).__name__}")
            if isinstance(symbol, gams.GamsSet):
                print("  Elements:")
                for record in symbol:
                    print(f"    {record.key(0)}")
            elif isinstance(symbol, gams.GamsParameter):
                print("  Values:")
                if len(symbol.domains) == 2:  # Check if the parameter has two-dimensional indices
                    for record in symbol:
                        print(f"    {record.keys[0]}-{record.keys[1]}: {record.value}")
                else:
                    try:
                        for record in symbol:
                            print(f"    {record.key(0)}: {record.value}")
                    except Exception as e:
                        print(f"    Error accessing values: {e}")
            else:
                print("  Unknown type")
                
    # Export data from GDX to Excel
print("[DEBUG 69] Entering function: export_to_excel")
def export_to_excel(gdxxrw_path, gdx_file_path, excel_file_path):
        try:
            subprocess.run([gdxxrw_path, gdx_file_path, f"par={excel_file_path}", "rng=A1", "wbt=par", "wb=par"], check=True)
            print("Data exported successfully from GDX to Excel.")
        except subprocess.CalledProcessError as e:
            print(f"Error exporting data from GDX to Excel: {e}")
            
    # Read data from GDX file, process it, and export results back to GDX
print("[DEBUG 70] Entering function: process_gdx_data")
def process_gdx_data(gdx_file_path, output_file_path):
        db = ws.add_database()
        db.execute_load(gdx_file_path)
        
        # Process data, perform calculations, etc. (as in your script)
        
        # Export results back to GDX file
        db_out = ws.add_database()
        # Add results to db_out
        db_out.export(output_file_path)
        print("Results exported successfully to GDX.")
        
    # Verify GDX contents
    verify_gdx_contents(gdx_file_path)
    
    # Export data from GDX to Excel
    gdxxrw_path = os.path.join(gams_system_directory, 'gdxxrw.exe')
    excel_file_path = 'input.xlsx'
    export_to_excel(gdxxrw_path, gdx_file_path, excel_file_path)
    
    # Process GDX data and export results back to GDX
    process_gdx_data(gdx_file_path, output_gdx)
    
    
    
    # Get symbols from the GDX file
    topology_data = db.get_symbol("Topology")
    link_delay_data = db.get_symbol("LinkDelay")
    app_definition_data = db.get_symbol("App_Definition")
    cpu_req_data = db.get_symbol("CPU_Req")
    bw_req_data = db.get_symbol("BW_Req")
    users_ap_data = db.get_symbol("Users_AP")
    users_app_data = db.get_symbol("Users_App")
    host_utilization_cap_data = db.get_symbol("HostUtilizationCap")
    scs_data = db.get_symbol("SCs")
    m_data = db.get_symbol("M")
    link_cap_data = db.get_symbol("LinkCap")
    user_bw_data = db.get_symbol("UserBW")
    
    # Populate parameters
    topology = {element[0]: element[1] for element in topology_data}
    link_delay = {link[0]: link[1] for link in link_delay_data}
    app_definition = {app[0]: app[1] for app in app_definition_data}
    cpu_req = {node[0]: node[1] for node in cpu_req_data}
    bw_req = {user_node[0]: user_node[1] for user_node in bw_req_data}
    users_ap = {user_node[0]: user_node[1] for user_node in users_ap_data}
    users_app = {user_app[0]: user_app[1] for user_app in users_app_data}
    host_utilization_cap = {node[0]: node[1] for node in host_utilization_cap_data}
    scs = {sc[0]: sc[1] for sc in scs_data}
    m = {key[0]: key[1] for key in m_data}
    link_cap = {link[0]: link[1] for link in link_cap_data}
    user_bw = {user[0]: user[1] for user in user_bw_data}
    
    # Initialize data structures to hold server and link states
    server_utilization = defaultdict(lambda: {'cpu': 0.0, 'memory': 0.0, 'storage': 0.0})
    link_utilization = defaultdict(float)
    accepted_users_count = 0
    rejected_users_count = 0
    total_routing_cost = 0.0
    link_cost = defaultdict(float)
    total_propagation_delay = 0.0
    total_edge_servers_used = 0
    total_cloud_servers_used = 0
    total_cost = 0
    
    # Define a function to find a feasible path for a user
print("[DEBUG 71] Entering function: find_feasible_path")
def find_feasible_path(G, source, target, bandwidth):
        for path in nx.all_simple_paths(G, source=source, target=target, cutoff=10):  # cutoff is optional, for performance
            can_use_path = True
            for i in range(len(path) - 1):
                link = (path[i], path[i + 1])
                if link_utilization[link] + bandwidth > link_cap[link]:
                    can_use_path = False
                    break
            if can_use_path:
                return path
        return None
        
    # Process each user
    for user, app in users_app.items():
        user_node = users_ap[user]  # Get the node associated with the user
        bandwidth = user_bw[user]  # Get the bandwidth requirement for the user
        
        # Check if the user's node has sufficient CPU capacity
        if server_utilization[user_node]['cpu'] + cpu_req[user_node] <= host_utilization_cap[user_node]:
            # Find a feasible path for the user
            path = find_feasible_path(topology, user_node, app_definition[app], bandwidth)
            if path:
                # Update link utilization and total routing cost along this path
                for i in range(len(path) - 1):
                    link = (path[i], path[i + 1])
                    link_utilization[link] += bandwidth
                    total_routing_cost += link_delay[link] * bandwidth
                # Update server utilization
                server_utilization[user_node]['cpu'] += cpu_req[user_node]
                accepted_users_count += 1
            else:
                rejected_users_count += 1
        else:
            rejected_users_count += 1
            
    # Calculate total propagation delay
    for user in users_ap.keys():
        user_node = users_ap[user]
        user_app = users_app[user]
        propagation_delay = link_delay.get((user_node, app_definition[user_app]), 0)
        total_propagation_delay += propagation_delay
        
    # Calculate total edge and cloud servers used
    total_edge_servers_used = sum(1 for node in server_utilization if 'cloud' not in node.lower())
    total_cloud_servers_used = sum(1 for node in server_utilization if 'cloud' in node.lower())
    
    # Calculate total cost
    total_cost = total_routing_cost + sum(host_utilization_cap.values())
    
    # Write results back to a GDX file if needed
    output_file_path = output_gdx
    db_out = ws.add_database()
    accepted_users_set = db_out.add_set("AcceptedUsers")
    rejected_users_set = db_out.add_set("RejectedUsers")
    total_prop_delay_set = db_out.add_set("TotalPropDelay")
    total_edge_servers_set = db_out.add_set("TotalEdgeServers")
    total_cloud_servers_set = db_out.add_set("TotalCloudServers")
    total_cost_set = db_out.add_set("TotalCost")
    accepted_users_set.add_record().value = accepted_users_count
    rejected_users_set.add_record().value = rejected_users_count
    total_prop_delay_set.add_record().value = total_propagation_delay
    total_edge_servers_set.add_record().value = total_edge_servers_used
    total_cloud_servers_set.add_record().value = total_cloud_servers_used
    total_cost_set.add_record().value = total_cost
    db_out.export(output_file_path)
    
    # Print some results
    print("User Acceptance Results:")
    print(f"Accepted Users: {accepted_users_count}")
    print(f"Rejected Users: {rejected_users_count}")
    print(f"Total Propagation Delay: {total_propagation_delay} ms")
    print(f"Total Edge Servers Used: {total_edge_servers_used}")
    print(f"Total Cloud Servers Used: {total_cloud_servers_used}")
    print(f"Total Cost: {total_cost}")
    
    
    
    # ## Create Test GDX File
    
    
    import os
    from gams import GamsWorkspace, GamsParameter
    from collections import defaultdict
    import networkx as nx
    
    # Define paths and settings
    gams_system_directory = 'C:\\GAMS\\win64\\24.9'
    gdx_file_path = 'data.gdx'
    output_gdx = 'Optimization_output.gdx'
    current_directory = os.getcwd()
    
    # Initialize GAMS workspace
    ws = GamsWorkspace(system_directory=gams_system_directory, working_directory=current_directory)
    
    # Read data from the GDX file and print contents
    db = ws.add_database_from_gdx(gdx_file_path)
    print("Contents of the GDX file before creating a new GDX file:")
    for symbol in db:
        print(f"Symbol: {symbol.name}")
        for record in symbol:
            print(record)
        print()
        
        
    #
    # Read data from the GDX file and print contents
    db = ws.add_database_from_gdx(gdx_file_path)
    for symbol in db:
        print(f"Symbol: {symbol.name}")
        for record in symbol:
            print(record)
        print()
        
    # Get symbols from the GDX file
    topology_data = db.get_symbol("Topology")
    link_delay_data = db.get_symbol("LinkDelay")
    cpu_req_data = db.get_symbol("CPU_Req")
    bw_req_data = db.get_symbol("BW_Req")
    users_ap_data = db.get_symbol("Users_AP")
    users_app_data = db.get_symbol("Users_App")
    host_utilization_cap_data = db.get_symbol("HostUtilizationCap")
    link_cap_data = db.get_symbol("LinkCap")
    user_bw_data = db.get_symbol("UserBW")
    
    
    # Initialize data structures to hold server and link states
    server_utilization_adaptive = defaultdict(lambda: {'cpu': 0.0, 'memory': 0.0, 'storage': 0.0})
    link_utilization_adaptive = defaultdict(float)
    link_cost_adaptive = defaultdict(float)
    total_routing_cost_adaptive = 0.0
    total_propagation_delay_adaptive = 0.0
    accepted_users_count_adaptive = 0
    rejected_users_count_adaptive = 0
    
    # Initialize additional counters
    total_edge_servers_used_adaptive = 0
    total_cloud_servers_used_adaptive = 0
    total_cost_adaptive = 0.0
    
    # Populate parameters
    topology = {element[0]: element[1] for element in topology_data}
    link_delay = {link[0]: link[1] for link in link_delay_data}
    cpu_req = {node[0]: node[1] for node in cpu_req_data}
    bw_req = {user_node[0]: user_node[1] for user_node in bw_req_data}
    users_ap = {user_node[0]: user_node[1] for user_node in users_ap_data}
    users_app = {user_app[0]: user_app[1] for user_app in users_app_data}
    host_utilization_cap = {node[0]: node[1] for node in host_utilization_cap_data}
    link_cap = {link[0]: link[1] for link in link_cap_data}
    user_bw = {user[0]: user[1] for user in user_bw_data}
    
    # Define a function to find a feasible path for a user
print("[DEBUG 72] Entering function: find_feasible_path")
def find_feasible_path(G, source, target, bandwidth):
        for path in nx.all_simple_paths(G, source=source, target=target, cutoff=10):  # cutoff is optional, for performance
            can_use_path = True
            for i in range(len(path) - 1):
                link = (path[i], path[i + 1])
                if link_utilization_adaptive[link] + bandwidth > link_cap[link]:
                    can_use_path = False
                    break
            if can_use_path:
                return path
        return None
        
    # Process each user
    for user, app in users_app.items():
        user_node = users_ap[user]  # Get the node associated with the user
        bandwidth = user_bw[user]  # Get the bandwidth requirement for the user
        
        # Check if the user's node has sufficient CPU capacity
        if server_utilization_adaptive[user_node]['cpu'] + cpu_req[user_node] <= host_utilization_cap[user_node]:
            # Find a feasible path for the user
            path = find_feasible_path(topology, user_node, app, bandwidth)
            if path:
                # Update link utilization and total routing cost along this path
                for i in range(len(path) - 1):
                    link = (path[i], path[i + 1])
                    link_utilization_adaptive[link] += bandwidth
                    total_routing_cost_adaptive += link_delay[link] * bandwidth
                # Update server utilization
                server_utilization_adaptive[user_node]['cpu'] += cpu_req[user_node]
                accepted_users_count_adaptive += 1
            else:
                rejected_users_count_adaptive += 1
        else:
            rejected_users_count_adaptive += 1
            
    # Calculate total propagation delay
    for user in users_ap.keys():
        user_node = users_ap[user]
        app = users_app[user]
        propagation_delay = link_delay.get((user_node, app), 0)
        total_propagation_delay_adaptive += propagation_delay
        
    # Calculate total edge and cloud servers used
    total_edge_servers_used_adaptive = sum(1 for node in server_utilization_adaptive if 'cloud' not in node.lower())
    total_cloud_servers_used_adaptive = sum(1 for node in server_utilization_adaptive if 'cloud' in node.lower())
    
    # Calculate total cost
    total_cost_adaptive = total_routing_cost_adaptive + sum(host_utilization_cap.values())
    
    # Write results back to a GDX file
    output_file_path = output_gdx
    db_out = ws.add_database()
    accepted_users_set = db_out.add_set("AcceptedUsers")
    rejected_users_set = db_out.add_set("RejectedUsers")
    total_prop_delay_set = db_out.add_set("TotalPropDelay")
    total_edge_servers_set = db_out.add_set("TotalEdgeServers")
    total_cloud_servers_set = db_out.add_set("TotalCloudServers")
    total_cost_set = db_out.add_set("TotalCost")
    accepted_users_set.add_record().value = accepted_users_count_adaptive
    rejected_users_set.add_record().value = rejected_users_count_adaptive
    total_prop_delay_set.add_record().value = total_propagation_delay_adaptive
    total_edge_servers_set.add_record().value = total_edge_servers_used_adaptive
    total_cloud_servers_set.add_record().value = total_cloud_servers_used_adaptive
    total_cost_set.add_record().value = total_cost_adaptive
    db_out.export(output_file_path)
    
    # Print some results
    print("User Acceptance Results:")
    print(f"Accepted Users: {accepted_users_count_adaptive}")
    print(f"Rejected Users: {rejected_users_count_adaptive}")
    print(f"Total Propagation Delay: {total_propagation_delay_adaptive} ms")
    print(f"Total Edge Servers Used: {total_edge_servers_used_adaptive}")
    print(f"Total Cloud Servers Used: {total_cloud_servers_used_adaptive}")
    print(f"Total Cost: {total_cost_adaptive}")
    
    
