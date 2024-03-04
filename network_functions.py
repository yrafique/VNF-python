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

############ READ XML FUNCTIONS #########
def read_nodes(nodelist):
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

def read_links(linklist):
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

def read_demands(demandlist):
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

def read_XMLnetwork(filename):
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


def calculate_distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def populate_network(G, nodes, links, medium='fiber'):
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




def draw_network_graph(G):
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

def print_link_attributes(G):
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

def print_node_attributes(G):
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

def measure_network_stats(G):
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
def find_nearest_ap(G, user_pos):
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


def create_users(G, NoOfUsers, node_range=50):
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
                    G_users.add_node(user_id, user=user_instance)  # Store the User instance
                    user_connections.append(((randx, randy), G.nodes[nearest_ap]['pos']))
                    user_count += 1
                if user_count >= NoOfUsers:
                    break
    return G_users, users, user_connections





################### SERVER FUNCTIONS ####################


def associate_edge_devices(G, edge_devices_filename, cloud_server_cost, edge_server_cost):
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


def print_edge_device_attributes(G):
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



def associate_user_devices(G_users, traffic_json_path):
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






def print_user_device_attributes(G_users):
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






def associate_app_with_containers(G_users, containers_json_path):
    print("Starting container association process...")

    # Load container data from JSON
    with open(containers_json_path, 'r') as f:
        containers_data = json.load(f)
    
    app_objects = {}  # Dictionary to store application objects

    # Loop through each user in G_users and update app_to_users mapping
    for user_id, attrs in G_users.nodes(data=True):
        user = attrs.get('user')  # Ensure this is a User instance
        if user and user.application:  # Check if the user and application are properly set
            app_name = user.application.name
            if app_name not in app_objects:
                app_objects[app_name] = user.application  # Assign the application object to app_objects
            app_objects[app_name].add_user(user)  # Add this user to the application's user list

    # Now, map each application to its containers
    for app_data in containers_data:
        app_name = app_data['application']
        if app_name in app_objects:
            app = app_objects[app_name]
            # Create and add CNF instances for each container in the application
            for cnf_data in (app_data['vnfs'] + app_data['microservices']):
                cnf = CNF(name=cnf_data['name'], cpu=float(cnf_data['cpu']), memory=float(cnf_data['memory']), storage=float(cnf_data['storage']), type='CNF')
                app.add_cnf(cnf)  # Add this CNF to the application

    print("Container association process completed.")
    return app_objects  # Return dictionary of Application objects






def print_applications_and_resources(app_objects):
    for app_name, app in app_objects.items():
        table = PrettyTable()
        table.field_names = ["Attribute", "Value"]
        table.add_row(["Application Name", app_name])
        table.add_row(["Associated Users", ', '.join(app.users)])
        table.add_row(["Total CPU (GHz)", sum(cnf.cpu for cnf in app.cnfs)])
        table.add_row(["Total Memory (GB)", sum(cnf.memory for cnf in app.cnfs)])
        table.add_row(["Total Storage (GB)", sum(cnf.storage for cnf in app.cnfs)])
        table.add_row(["Service Function Chain", ', '.join(cnf.name for cnf in app.cnfs)])
        print(table)
        print("---------------------------------------------------")
