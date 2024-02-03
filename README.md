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
