# Filename: traffic_volume_allocation.py
# Description: This file contains the code for allocating traffic volume to microservices.

# Class to represent Traffic Volume
class TrafficVolume:
    def __init__(self, name, volume):
        self.name = name  # Name of the application
        self.volume = volume  # Traffic volume in Gbps

# Function to allocate traffic volume to microservices
def allocate_traffic_volume_to_microservices(apps, microservices):
    """Allocate traffic volume to microservices based on their application."""
    allocations = {}
    for app in apps:
        for ms in microservices:
            if ms.app_name == app.name:
                allocations[ms.name] = app.volume
    return allocations

# Test function
def test_allocate_traffic_volume_to_microservices():
    """Test the allocate_traffic_volume_to_microservices function."""
    app1 = TrafficVolume("Traffic Monitoring", 10)
    app2 = TrafficVolume("Weather Forecast", 5)

    ms1 = Microservice("Traffic Data Processing", "Traffic Monitoring", 2, 4)
    ms2 = Microservice("Weather Data Analysis", "Weather Forecast", 1, 2)

    result = allocate_traffic_volume_to_microservices([app1, app2], [ms1, ms2])
    
    assert result["Traffic Data Processing"] == 10
    assert result["Weather Data Analysis"] == 5

    print("All tests passed!")

# Sample print statement
test_allocate_traffic_volume_to_microservices()
print(f"Traffic volume allocated to Microservices: {allocate_traffic_volume_to_microservices([TrafficVolume('Traffic Monitoring', 10), TrafficVolume('Weather Forecast', 5)], [Microservice('Traffic Data Processing', 'Traffic Monitoring', 2, 4), Microservice('Weather Data Analysis', 'Weather Forecast', 1, 2)])}")

# Output of test function
# All tests passed!
# Traffic volume allocated to Microservices: {'Traffic Data Processing': 10, 'Weather Data Analysis': 5}
