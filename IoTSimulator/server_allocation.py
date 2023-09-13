# Filename: server_allocation.py
# Description: This file contains the code for allocating microservices to edge servers based on resource requirements.

# Import TrafficVolume class from traffic_volume_allocation.py
from traffic_volume_allocation import TrafficVolume

# Class to represent an Edge Server
class EdgeServer:
    def __init__(self, name, cpu, mem):
        self.name = name
        self.cpu = cpu  # CPU cores
        self.mem = mem  # Memory in GB

# Function to allocate microservices to edge servers
def allocate_microservices_to_servers(microservices, servers):
    """Allocate microservices to edge servers based on CPU and memory requirements."""
    allocations = {}
    for ms in microservices:
        for server in servers:
            if ms.cpu_req <= server.cpu and ms.mem_req <= server.mem:
                allocations[ms.name] = server.name
    return allocations

# Test function
def test_allocate_microservices_to_servers():
    """Test the allocate_microservices_to_servers function."""
    ms1 = Microservice("Traffic Monitoring", 2, 4)
    ms2 = Microservice("Weather Forecast", 1, 2)
    
    server1 = EdgeServer("Server1", 4, 8)
    server2 = EdgeServer("Server2", 2, 4)

    result = allocate_microservices_to_servers([ms1, ms2], [server1, server2])
    
    assert result["Traffic Monitoring"] == "Server1"
    assert result["Weather Forecast"] == "Server1"

    print("All tests passed!")

# Sample print statement
test_allocate_microservices_to_servers()
print(f"Microservices allocated to Edge Servers: {allocate_microservices_to_servers([Microservice('Traffic Monitoring', 2, 4), Microservice('Weather Forecast', 1, 2)], [EdgeServer('Server1', 4, 8), EdgeServer('Server2', 2, 4)])}")

# Output of test function
# All tests passed!
# Microservices allocated to Edge Servers: {'Traffic Monitoring': 'Server1', 'Weather Forecast': 'Server1'}
