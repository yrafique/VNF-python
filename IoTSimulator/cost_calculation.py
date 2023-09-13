# cost_calculation.py
# This file calculates the cost for hosting a microservice on a server

from server import Server
from microservice import Microservice

class ServerCost:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


# Function to calculate the cost
def calculate_cost(server, microservice):
    # Your cost calculation logic here
    cpu_cost = server.cpu * 10  # Hypothetical cost logic
    ram_cost = server.ram * 5  # Hypothetical cost logic
    total_cost = cpu_cost + ram_cost
    return total_cost

# Test function to test the calculate_cost function
def test_calculate_cost():
    # Initialize a server with the missing 'latency' argument
    server = Server("AWS-EC2", 4, 8, 100, 10, 1)  # name, cpu, ram, storage, bandwidth, latency
    
    # Initialize a microservice
    microservice = Microservice("Traffic Data Processing", "Traffic Monitoring", 2, 4, "AWS-EC2", 1, 100)  # additional arguments for latency_sensitivity and bandwidth_requirement
    
    # Calculate cost
    cost = calculate_cost(server, microservice)
    
    # Print the result
    print(f"The calculated cost for hosting the microservice on the server is: ${cost} USD.")

# Output for testing purposes
if __name__ == "__main__":
    test_calculate_cost()
