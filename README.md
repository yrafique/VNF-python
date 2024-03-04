# VNF-python
 
# Network Simulator Visualization Tool

This Python-based tool provides visual insights into various aspects of a network simulator. It focuses on server utilization, link utilization, and user acceptance in a simulated network environment.

## Features and Functionalities

| Feature           | Description                                                             | Visualization Type |
|-------------------|-------------------------------------------------------------------------|--------------------|
| Server Utilization| Displays the CPU, Memory, and Storage utilization of different servers. | Bar Graph          |
| Link Utilization  | Shows the bandwidth utilization of different network links.             | Bar Graph          |
| User Acceptance   | Visualizes the percentage of accepted and rejected users.               | Bar Graph          |

## Visualization Details

### Server Utilization Graph:
- **X-axis:** Individual servers
- **Y-axis:** Utilization metrics (CPU in GHz, Memory in GB, Storage in GB)
- **Color-coded bars:** Blue for CPU, Cyan for Memory, Magenta for Storage

### Link Utilization Graph:
- **X-axis:** Network links (formatted as 'Node1-Node2')
- **Y-axis:** Bandwidth utilization in Mbps
- **Red bars** represent the bandwidth utilization

### User Acceptance Graph:
- **X-axis:** User status categories ('Accepted Users', 'Rejected Users')
- **Y-axis:** Percentage of users in each category
- **Color-coded bars:** Green for Accepted Users, Red for Rejected Users

## Customization
- The Y-axis maximum for the User Acceptance Graph can be adjusted as needed.



# Network Functions

This Python module, `network_functions.py`, is designed to assist with parsing network data from XML files and manipulating network structures using the NetworkX library. It provides a range of functionalities aimed at network analysis and visualization, making it a valuable tool for researchers, engineers, and network analysts.

## Installation

Before using `network_functions.py`, ensure you have Python 3.x installed on your system. Additionally, the script depends on several external libraries. You can install all required libraries using pip:

```bash
pip install networkx pandas numpy scipy matplotlib prettytable
```

## Features

The module includes the following key features:

- **XML Network Data Parsing**: Functions to parse network nodes, links, and demands from XML files.
- **NetworkX Graph Operations**: Utilities to populate, manipulate, and visualize NetworkX graphs.
- **Network Analysis Tools**: Functions to analyze network statistics, efficiency, and connectivity.
- **User and Server Management**: Tools for associating users and servers within network structures.

## Usage

Here's how to use the main functionalities of the module:

### Parsing XML Network Data

To parse network data from an XML file:

```python
from network_functions import read_XMLnetwork

nodes, links, demands = read_XMLnetwork('path_to_your_network_data.xml')
```

### Populating and Visualizing a NetworkX Graph

To populate a NetworkX graph with nodes and links and then visualize it:

```python
import networkx as nx
from network_functions import populate_network, draw_network_graph

# Initialize a new NetworkX graph
G = nx.Graph()

# Populate the graph
populate_network(G, nodes, links)

# Visualize the graph
draw_network_graph(G)
```

### Analyzing Network Statistics

To analyze and print various network statistics:

```python
from network_functions import measure_network_stats

measure_network_stats(G)
```

### Managing Users and Servers

To create users and associate them with the nearest access point:

```python
from network_functions import create_users

G_users, users, user_connections = create_users(G, NoOfUsers=10)
```

To associate edge devices with servers based on JSON data:

```python
from network_functions import associate_edge_devices

associate_edge_devices(G, 'path_to_edge_devices.json', cloud_server_cost=100, edge_server_cost=50)
```

## Examples

For more detailed examples and use cases, please refer to the `examples` directory in this repository.

## Contribution

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file in this repository for full license text.

