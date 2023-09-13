# Filename: microservice_allocation.py
# Description: This file contains the code for allocating microservices to edge servers 
# based on device classification and microservice requirements.

# Class to represent a Microservice
class Microservice:
    def __init__(self, name, cpu_req, mem_req):
        self.name = name
        self.cpu_req = cpu_req  # CPU requirement in GHz
        self.mem_req = mem_req  # Memory requirement in GB

# Function to allocate microservices to devices
def allocate_microservice(device, microservices):
    """Allocate microservices to edge servers or edge nodes."""
    if device == "Edge Server":
        return [ms for ms in microservices if ms.cpu_req <= 4 and ms.mem_req <= 16]
    elif device == "Edge Node":
        return [ms for ms in microservices if ms.cpu_req <= 2 and ms.mem_req <= 8]
    else:
        return []

# Test function
def test_allocate_microservice():
    """Test the allocate_microservice function."""
    ms1 = Microservice("Traffic Monitoring", 2, 4)
    ms2 = Microservice("Weather Forecast", 1, 2)
    ms3 = Microservice("Facial Recognition", 3, 6)
    
    device1 = "Edge Server"
    device2 = "Edge Node"
    device3 = "Edge Gateway"

    assert len(allocate_microservice(device1, [ms1, ms2, ms3])) == 3
    assert len(allocate_microservice(device2, [ms1, ms2])) == 2
    assert len(allocate_microservice(device3, [ms1, ms2, ms3])) == 0

    print("All tests passed!")

# Sample print statement
test_allocate_microservice()
print(f"Microservices allocated to Edge Server: {[ms.name for ms in allocate_microservice('Edge Server', [Microservice('Traffic Monitoring', 2, 4), Microservice('Weather Forecast', 1, 2), Microservice('Facial Recognition', 3, 6)])]}")
