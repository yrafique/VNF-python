import sys
import xml.dom.minidom as minidom
import string
from xml.dom import minidom
from xml.dom.minidom import parse
import os

# Read Nodes from XML
def read_nodes(nodelist) -> dict:
    nodes = {}
    for i, node in enumerate(nodelist):
        node_id = i + 1
        Nodeid = node.getAttribute("id")
        x_cor = float(node.getElementsByTagName('x')[0].firstChild.data)
        y_cor = float(node.getElementsByTagName('y')[0].firstChild.data)
        nodes[node_id] = {'id': Nodeid, 'x_cor': x_cor, 'y_cor': y_cor}
    return nodes

# Read Links from XML
def read_links(linklist):
    links = {}
    for i, link in enumerate(linklist):
        link_id = i + 1  # Assuming link IDs start from 1 and are sequential integers
        source = link.getElementsByTagName("source")[0].firstChild.data
        destination = link.getElementsByTagName("target")[0].firstChild.data
        
        print(f"Debug: Link {link_id} - Source: {source}, Destination: {destination}")  # Debug print
        
        # ... (rest of your code)

        additionalModules = link.getElementsByTagName('additionalModules')[0]
        addModule = additionalModules.getElementsByTagName('addModule')[0]
        capacity = float(addModule.getElementsByTagName('capacity')[0].firstChild.data)
        cost = float(addModule.getElementsByTagName('cost')[0].firstChild.data)
        links[link_id] = {'source': source, 'destination': destination, 'capacity': capacity, 'cost': cost}
    return links

# Read Demands from XML
def read_demands(demandlist) -> dict:
    demands = {}
    for i, demand in enumerate(demandlist):
        demand_id = i + 1
        source = demand.getElementsByTagName('source')[0].firstChild.data
        destination = demand.getElementsByTagName('target')[0].firstChild.data
        demandValue = float(demand.getElementsByTagName('demandValue')[0].firstChild.data)
        demands[demand_id] = {'source': source, 'destination': destination, 'demandValue': demandValue}
    return demands

# Function that will be called to read networks from other files
def read_XMLnetwork(filename: str):
    Read_Data = minidom.parse(filename)
    nodes = read_nodes(Read_Data.getElementsByTagName('node'))
    links = read_links(Read_Data.getElementsByTagName('link'))
    demands = read_demands(Read_Data.getElementsByTagName('demand'))
    return nodes, links, demands

# Print Read File
def print_test(network_name: str, nodes: dict, links: dict, demands: dict):
    print(f'\n\nNetwork Name: {network_name}')
    print('\n**** Nodes read: ******\n')
    for node_id, node_data in nodes.items():
        print(f"Node #\t{node_id}: \t{node_data['id'].ljust(20)}\tx: {node_data['x_cor']}, \ty: {node_data['y_cor']}")

    print('\n**** Links read: ******\n')
    for link_id, link_data in links.items():
        print(f"Link #\t{link_id}, From: {link_data['source'].ljust(15)}, To: {link_data['destination'].ljust(15)},\tCapacity: {link_data['capacity']}, \tCost: {link_data['cost']}")

# Main function for testing
if __name__ == "__main__":
    filename = "your_file.xml"  # Replace with your actual XML filename
    nodes, links, demands = read_XMLnetwork(filename)
    print_test("your_network_name", nodes, links, demands)  # Replace 'your_network_name' with the actual network name
