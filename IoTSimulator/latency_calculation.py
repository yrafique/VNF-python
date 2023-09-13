# File Name: latency_calculation.py
# This file calculates the latency for microservices based on the server they are allocated to.

from server import Server
from microservice import Microservice
from server_selection import select_server
from random import randint

# Function to calculate latency
def calculate_latency(server, microservice):
    latency = server.latency * microservice.latency_sensitivity
    return latency

# Test function
def test_calculate_latency():
    server1 = Server("AWS-EC2", 8, 16, 200, 1, 10)
    ms1 = Microservice("Traffic Data Processing", "Traffic Monitoring", 2, 4, "AWS-EC2", 0.2)
    
    latency = calculate_latency(server1, ms1)
    print(f"The latency for {ms1.name} on {server1.server_type} is {latency} ms.")

# Sample print output from test function
# The latency for Traffic Data Processing on AWS-EC2 is 2.0 ms.

if __name__ == "__main__":
    test_calculate_latency()
