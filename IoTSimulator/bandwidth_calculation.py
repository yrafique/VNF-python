# File Name: bandwidth_calculation.py
# This file calculates the bandwidth usage for microservices based on the server they are allocated to.

from server import Server
from microservice import Microservice
from server_selection import select_server

# Function to calculate bandwidth usage
def calculate_bandwidth(server, microservice):
    bandwidth = server.bandwidth * microservice.bandwidth_requirement
    return bandwidth

# Test function
def test_calculate_bandwidth():
    server1 = Server("AWS-EC2", 8, 16, 200, 1, 10)
    ms1 = Microservice("Traffic Data Processing", "Traffic Monitoring", 2, 4, "AWS-EC2", 0.2, 0.5)
    
    bandwidth = calculate_bandwidth(server1, ms1)
    print(f"The bandwidth usage for {ms1.name} on {server1.server_type} is {bandwidth} Gbps.")

# Sample print output from test function
# The bandwidth usage for Traffic Data Processing on AWS-EC2 is 5.0 Gbps.

if __name__ == "__main__":
    test_calculate_bandwidth()
