# network_functions.py
"""
This module provides functions for parsing network configurations from XML files and for 
manipulating and analyzing network structures using NetworkX, a Python library for 
the creation, manipulation, and study of complex networks.
"""

import networkx as nx
import numpy as np
import math
from scipy.spatial.distance import euclidean
import random
import json
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import xml.dom.minidom as dom
from network_classes import *
import logging

def read_nodes(nodelist, debug=False):
    nodes = {}
    for node in nodelist:
        node_id = node.getAttribute("id")
        x = float(node.getElementsByTagName('x')[0].firstChild.data)
        y = float(node.getElementsByTagName('y')[0].firstChild.data)
        nodes[node_id] = Node(node_id, x, y)
        debug_print(f"Processed node: ID={node_id}, x={x}, y={y}", debug)
    return nodes

def read_links(linklist, default_medium='fiber', debug=False):
    links = {}
    for link in linklist:
        link_id = link.getAttribute("id")
        source = link.getElementsByTagName("source")[0].firstChild.data
        target = link.getElementsByTagName("target")[0].firstChild.data
        capacity = float(link.getElementsByTagName("capacity")[0].firstChild.data)
        cost = float(link.getElementsByTagName("cost")[0].firstChild.data)
        medium_nodes = link.getElementsByTagName("medium")
        medium = medium_nodes[0].firstChild.data if medium_nodes else default_medium
        links[link_id] = Link(link_id, source, target, capacity, cost, medium)
        debug_print(f"Processed link: ID={link_id}, source={source}, target={target}, medium={medium}", debug)
    return links

def read_demands(demandlist, debug=False):
    demands = {}
    for demand in demandlist:
        demand_id = demand.getAttribute("id")
        source = demand.getElementsByTagName("source")[0].firstChild.data
        destination = demand.getElementsByTagName("target")[0].firstChild.data
        demandValue = float(demand.getElementsByTagName("demandValue")[0].firstChild.data)
        demands[demand_id] = Demand(demand_id, source, destination, demandValue)
        debug_print(f"Processed demand: ID={demand_id}, source={source}, destination={destination}", debug)
    return demands

def populate_network(G, filename, default_medium='fiber', debug=False):
    Node, links, _ = read_XMLnetwork(filename, debug)
    propagation_speeds = {
        'fiber': 200, 'ethernet': 200, 'wifi': 300, '5g': 300, 'lora': 300, 'p2p_microwave': 300
    }
    for node_id, node in nodes.items():
        G.add_node(node_id, pos=(node.x, node.y), **vars(node))
        debug_print(f"Added node: ID={node_id} with position=({node.x}, {node.y})", debug)
    for link_id, link in links.items():
        source_pos = G.nodes[link.source]['pos']
        target_pos = G.nodes[link.target]['pos']
        distance = calculate_distance(*source_pos, *target_pos)
        medium = getattr(link, 'medium', default_medium)
        speed = propagation_speeds[medium]
        latency = distance / speed
        G.add_edge(link.source, link.target, capacity=link.capacity, cost=link.cost, latency=latency, medium=medium)
        debug_print(f"Added link: ID={link_id} from {link.source} to {link.target} with medium={medium}", debug)


# NetworkX Graph Functions
def calculate_distance(x1, y1, x2, y2):
    """
    Calculate the Euclidean distance between two points.
    Args:
        x1, y1, x2, y2 (float): Coordinates of the two points.
    Returns:
        float: Euclidean distance between the two points.
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)





def draw_network_graph(G, mec_location=None):
    """
    Draws the network graph using NetworkX and Matplotlib, highlighting the MEC server.

    Args:
        G (networkx.Graph): The graph to draw.
        mec_location (tuple): The (x, y) coordinates of the MEC server, if present.
    """
    import matplotlib.pyplot as plt

    # Draw the regular network nodes and edges
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=12)

    # Highlight and label the MEC server distinctly
    if mec_location:
        nx.draw_networkx_nodes(G, pos, nodelist=[mec_location], node_size=600, node_color='red')
        nx.draw_networkx_labels(G, pos, labels={mec_location: 'MEC Server'}, font_color='white')

    plt.title('Network Topology')
    plt.show()


def print_link_attributes(G):
    """
    Prints the attributes of each link in the network graph.
    Args:
        G (networkx.Graph): The graph containing the links.
    """
    link_table = PrettyTable(["Edge", "Capacity (Mbps)", "Cost", "Propagation Delay (ms)", "Medium"])
    for (u, v, attrs) in G.edges(data=True):
        link_table.add_row([f"{u} to {v}", attrs['capacity'], attrs['cost'], attrs.get('latency', 'N/A'), attrs.get('medium', 'N/A')])
    print("Graph Edges and their Attributes:")
    print(link_table)

def print_node_attributes(G):
    """
    Prints the attributes of each node in the network graph.
    Args:
        G (networkx.Graph): The graph containing the nodes.
    """
    node_table = PrettyTable(["Node", "x-coordinate", "y-coordinate", "Medium"])
    for node, attrs in G.nodes(data=True):
        x, y = attrs['pos']
        node_table.add_row([node, x, y, attrs.get('medium', 'N/A')])
    print("Graph Nodes and their Attributes:")
    print(node_table)

# User and Application Functions
def find_nearest_ap(G, user_pos):
    """
    Finds the nearest access point to a given user position in the network.
    Args:
        G (networkx.Graph): The graph representing the network.
        user_pos (tuple): The (x, y) coordinates of the user.
    Returns:
        tuple: The ID and position (x, y) of the nearest access point. Returns (None, None) if no AP found.
    """
    min_distance = float('inf')
    nearest_ap = None
    nearest_pos = None
    for ap, data in G.nodes(data=True):
        ap_pos = data['pos']
        distance = euclidean(user_pos, ap_pos)
        if distance < min_distance:
            min_distance = distance
            nearest_ap = ap
            nearest_pos = ap_pos
    return nearest_ap, nearest_pos




def create_users(G, NoOfUsers, node_range=50):
    """
    Creates a specified number of user nodes, each associated with the nearest access point.
    Args:
        G (networkx.Graph): The graph representing the network infrastructure.
        NoOfUsers (int): The number of user nodes to create.
        node_range (float): The maximum distance from network nodes within which users can be placed.
    Returns:
        tuple: A graph containing user nodes, a list of User instances, and a list of user connections.
    """
    G_users = nx.Graph()
    user_connections = []
    users = []
    user_count = 0

    while user_count < NoOfUsers:
        for node in G.nodes(data=True):
            if node[1].get('type') != 'cloud':  # Assuming 'type' is used to differentiate nodes, skip cloud nodes
                node_pos = node[1]['pos']
                randx = random.uniform(node_pos[0] - node_range, node_pos[0] + node_range)
                randy = random.uniform(node_pos[1] - node_range, node_pos[1] + node_range)
                user_pos = (randx, randy)
                nearest_ap, _ = find_nearest_ap(G, user_pos)

                if nearest_ap:
                    user_id = f"user_{user_count}"
                    user = User(user_id, user_pos, nearest_ap)  # Ensure associated_ap is passed here
                    users.append(user)
                    G_users.add_node(user_id, pos=user_pos, user=user)
                    user_connections.append((user_pos, G.nodes[nearest_ap]['pos']))
                    user_count += 1

                if user_count >= NoOfUsers:
                    break

    return G_users, users, user_connections



def print_user_details(users):
    """
    Prints details of all user instances.
    Args:
        users (list): List of User instances.
    """
    user_table = PrettyTable(["User ID", "Position", "Associated AP"])
    for user in users:
        user_table.add_row([user.id, user.pos, user.associated_ap])
    print("User Details:")
    print(user_table)

# Server Functions
def associate_edge_devices(G, edge_devices_filename, cloud_server_cost, edge_server_cost):
    """
    Updates the attributes of edge devices in the graph based on JSON data.
    Args:
        G (networkx.Graph): The graph representing the network.
        edge_devices_filename (str): Path to the JSON file containing edge device data.
        cloud_server_cost (float): Cost associated with cloud servers.
        edge_server_cost (float): Cost associated with edge servers.
    """
    with open(edge_devices_filename, 'r') as file:
        edge_devices_data = json.load(file)
    for node_id in G.nodes():
        if "cloud" in node_id.lower():  # Identify cloud nodes
            server_data = edge_devices_data.get('cloud', {})
            server_instance = Server(
                server_data.get('name', 'Unknown'), server_data.get('formFactor', None),
                server_data.get('architecture', 'Unknown'), server_data.get('cpu', 'Unknown'),
                server_data.get('memory', 'Unknown'), server_data.get('storage', 'Unknown'),
                'cloud', cloud_server_cost
            )
        else:  # Edge nodes
            server_data = edge_devices_data.get('edge', {})
            server_instance = Server(
                server_data.get('name', 'Unknown'), server_data.get('formFactor', None),
                server_data.get('architecture', 'Unknown'), server_data.get('cpu', 'Unknown'),
                server_data.get('memory', 'Unknown'), server_data.get('storage', 'Unknown'),
                'edge', edge_server_cost
            )
        G.nodes[node_id]['server'] = server_instance

def print_edge_device_attributes(G):
    """
    Prints attributes of edge devices in the graph.
    Args:
        G (networkx.Graph): The graph representing the network with edge devices.
    """
    edge_table = PrettyTable(["Node", "Server Name", "Form Factor", "Architecture", "CPU", "Memory", "Storage", "Cost"])
    for node, data in G.nodes(data=True):
        server = data.get('server')
        if server:
            edge_table.add_row([
                node, server.name, server.formFactor, server.architecture, 
                server.cpu, server.memory, server.storage, server.server_cost
            ])
    print("Edge Device Attributes:")
    print(edge_table)

# Application and Container Association Functions
def associate_app_with_containers(G_users, containers_json_path):
    """
    Associates applications with containers and users based on container data.
    Args:
        G_users (networkx.Graph): The graph representing user devices.
        containers_json_path (str): Path to the JSON file containing container data.
    Returns:
        dict: Dictionary of Application instances keyed by application name.
    """
    with open(containers_json_path, 'r') as file:
        container_data = json.load(file)
    
    app_objects = {}  # Stores application instances
    for app_data in container_data:
        # Create Application instances from container data
        app_name = app_data['application']
        if app_name not in app_objects:
            app_objects[app_name] = Application(
                name=app_name, bandwidth=app_data.get('bandwidth', 0),
                latency=app_data.get('latency', 0), device_density=app_data.get('device_density', 0),
                source='DefinedSource', sfc=app_data.get('sfc', [])
            )
        # Add CNFs to Application instance
        for cnf_data in app_data.get('cnfs', []):
            cnf_instance = CNF(
                name=cnf_data['name'], cpu=cnf_data['cpu'],
                memory=cnf_data['memory'], storage=cnf_data['storage']
            )
            app_objects[app_name].add_cnf(cnf_instance)
    
    # Associate users with applications
    for user_id, data in G_users.nodes(data=True):
        user_instance = data.get('user')
        if user_instance and user_instance.application:
            app_name = user_instance.application.name
            if app_name in app_objects:
                app_objects[app_name].add_user(user_instance)
    
    return app_objects

def print_applications_and_resources(app_objects):
    """
    Prints out the resources and users associated with each application.
    Args:
        app_objects (dict): Dictionary of Application instances keyed by application name.
    """
    for app_name, app_instance in app_objects.items():
        print(f"\nApplication: {app_name}")
        print(f"Bandwidth: {app_instance.bandwidth} Mbps, Latency: {app_instance.latency} ms")
        print("Users:", ', '.join([user.id for user in app_instance.users]))
        print("Containers:")
        for cnf in app_instance.cnfs:
            print(f"  {cnf.name}: CPU {cnf.cpu} GHz, Memory {cnf.memory} GB, Storage {cnf.storage} GB")

# Network Efficiency Functions
def calculate_network_efficiency(G):
    """
    Calculates and prints the overall efficiency of the network.
    Args:
        G (networkx.Graph): The network graph.
    """
    efficiency = nx.global_efficiency(G)
    print(f"\nNetwork Efficiency: {efficiency:.4f}")
    # The global efficiency is the average inverse shortest path length in the network

def evaluate_network_performance(G, app_objects):
    """
    Evaluates the network performance based on application requirements and network configuration.
    Args:
        G (networkx.Graph): The network graph.
        app_objects (dict): Dictionary of Application instances keyed by application name.
    """
    print("\nNetwork Performance Evaluation:")
    for app_name, app_instance in app_objects.items():
        print(f"Application: {app_name}")
        satisfied_users = 0
        for user in app_instance.users:
            path_length = nx.shortest_path_length(G, source=user.associated_ap, target='cloud_server')  # Example target
            if path_length <= app_instance.latency:  # Just an illustrative comparison
                satisfied_users += 1
        print(f"  Satisfied Users: {satisfied_users}/{len(app_instance.users)}")


def find_edge_servers(G):
    """
    Finds all edge servers in the graph based on a 'type' attribute.

    Args:
        G (networkx.Graph): The graph to search within.

    Returns:
        list: A list of node IDs that are edge servers.
    """
    edge_servers = [node for node, attrs in G.nodes(data=True) if attrs.get('type') == 'edge_server']
    return edge_servers





def calculate_geographic_midpoint(locations):
    """
    Calculate the geographic midpoint for a list of (x, y) coordinates.
    Args:
        locations (list): List of (x, y) coordinates.
    Returns:
        tuple: The (x, y) coordinates of the geographic midpoint.
    """
    x_coords, y_coords = zip(*locations)
    return (np.mean(x_coords), np.mean(y_coords))

def set_mec_server(G, edge_servers):
    """
    Sets the MEC (Mobile Edge Computing) server in the network graph based on the geographic midpoint of edge servers.
    
    Args:
        G (networkx.Graph): The network graph.
        edge_servers (list): A list of nodes representing edge servers in the network.
        
    Returns:
        tuple: The (x, y) coordinates of the MEC server.
    """
    if not edge_servers:
        raise ValueError("No edge servers provided to determine the MEC server location.")
    
    # Calculate the geographic midpoint based on edge servers' positions
    x_coords, y_coords = zip(*[G.nodes[edge_server]['pos'] for edge_server in edge_servers])
    mid_x, mid_y = np.mean(x_coords), np.mean(y_coords)
    
    # Add the MEC server to the graph with this midpoint position
    G.add_node('mec_server', pos=(mid_x, mid_y), type='MEC_server')
    
    # Return the position for further use
    return mid_x, mid_y

def set_mec_server_based_on_all_nodes(G):
    """
    Sets the MEC server in the graph based on the geographic midpoint of all nodes if no specific edge servers are identified.
    
    Args:
        G (networkx.Graph): The graph to update.
    
    Returns:
        tuple: The (x, y) coordinates of the newly set MEC server.
    """
    if G.number_of_nodes() == 0:
        raise ValueError("The graph contains no nodes.")
    
    # Calculate the geographic midpoint based on all nodes' positions
    x_coords, y_coords = zip(*[data['pos'] for node, data in G.nodes(data=True)])
    mid_x, mid_y = np.mean(x_coords), np.mean(y_coords)
    
    # Add the MEC server to the graph with this midpoint position
    G.add_node('mec_server', pos=(mid_x, mid_y), type='MEC_server')
    
    return mid_x, mid_y



def report_network_health(G):
    """
    Reports the health and statistics of the network.
    Args:
        G (networkx.Graph): The graph representing the network.
    """
    health_table = PrettyTable()
    health_table.field_names = ["Metric", "Value"]

    # Network connectivity (True if the graph is connected, False otherwise)
    health_table.add_row(["Connected", nx.is_connected(G)])

    # Network density
    health_table.add_row(["Density", nx.density(G)])

    # Average clustering coefficient
    health_table.add_row(["Average Clustering", nx.average_clustering(G)])

    # Network diameter (Only if the network is connected)
    if nx.is_connected(G):
        health_table.add_row(["Diameter", nx.diameter(G)])

    # Average shortest path length (Only if the network is connected)
    if nx.is_connected(G):
        health_table.add_row(["Avg Shortest Path Length", nx.average_shortest_path_length(G)])

    # Edge server details
    if 'mec_server' in G.nodes:
        mec_pos = G.nodes['mec_server']['pos']
        health_table.add_row(["MEC Server Position", mec_pos])
    else:
        health_table.add_row(["MEC Server Position", "Not set"])

    print(health_table)

def measure_network_stats(G):
    """
    Measure various statistics of the network.
    Args:
        G (networkx.Graph): The graph representing the network.
    """
    stats_table = PrettyTable()
    stats_table.field_names = ["Metric", "Value"]
    
    # Calculate PageRank
    pageranks = nx.pagerank(G)
    # Sort nodes by PageRank
    sorted_pageranks = sorted(pageranks.items(), key=lambda x: x[1], reverse=True)

    # Network complexity as number of edges
    stats_table.add_row(["Complexity (edges)", G.number_of_edges()])

    # Average shortest path (if network is connected)
    if nx.is_connected(G):
        stats_table.add_row(["Avg. Shortest Path Length", nx.average_shortest_path_length(G)])
    
    # Add more network statistics as needed

    print(stats_table)

    # Print top nodes by PageRank
    print("Top nodes by PageRank:")
    for node, rank in sorted_pageranks[:5]:  # Show top 5
        print(f"Node {node} has PageRank {rank:.4f}")


def draw_network_and_users(G, G_users, user_connections):
    """
    Draws the network graph including users and their nearest access points.
    
    Args:
        G (networkx.Graph): The graph representing the network infrastructure.
        G_users (networkx.Graph): The graph representing user devices.
        user_connections (list): A list of tuples representing connections between users and APs.
    """
    import matplotlib.pyplot as plt
    # Draw the main network nodes and edges
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue')

    # Draw edge servers distinctly if they are specified
    edge_servers = find_edge_servers(G)
    if edge_servers:
        nx.draw_networkx_nodes(G, pos, nodelist=edge_servers, node_size=800, node_color='green', label='Edge Server')

    # Draw MEC server distinctly if it exists
    if 'mec_server' in G.nodes:
        mec_pos = { 'mec_server': G.nodes['mec_server']['pos'] }
        nx.draw_networkx_nodes(G, mec_pos, nodelist=['mec_server'], node_size=1000, node_color='red', label='MEC Server')

    # Draw users
    pos_users = nx.get_node_attributes(G_users, 'pos')
    nx.draw_networkx_nodes(G_users, pos_users, node_size=300, node_color='red', node_shape='s', label='Users')

    # Draw connections between users and the network
    for user_pos, ap_pos in user_connections:
        plt.plot([user_pos[0], ap_pos[0]], [user_pos[1], ap_pos[1]], 'green', linestyle='dotted', linewidth=2.5)

    plt.legend()
    plt.title('Network and User Topology')
    plt.show()
