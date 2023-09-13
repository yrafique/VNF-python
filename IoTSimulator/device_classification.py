# Filename: device_classification.py
# Description: This file contains the code for classifying edge devices into 
# edge servers, edge nodes, and edge gateways based on their hardware capabilities.

# Class to represent a device
class Device:
    def __init__(self, name, cpu, memory, storage):
        self.name = name
        self.cpu = cpu  # CPU speed in GHz
        self.memory = memory  # Memory size in GB
        self.storage = storage  # Storage size in GB

# Function to classify devices
def classify_device(device):
    """Classify the device based on CPU, memory, and storage."""
    if device.cpu >= 4 and device.memory >= 16:
        return "Edge Server"
    elif device.cpu >= 2:
        return "Edge Node"
    else:
        return "Edge Gateway"

# Test function
def test_classify_device():
    """Test the classify_device function."""
    d1 = Device("Raspberry Pi", 1.5, 8, 16)
    d2 = Device("High-end Server", 8, 64, 256)
    d3 = Device("Regular PC", 2.5, 8, 128)
    
    assert classify_device(d1) == "Edge Gateway"
    assert classify_device(d2) == "Edge Server"
    assert classify_device(d3) == "Edge Node"

    print("All tests passed!")

# Sample print statement
test_classify_device()
print(f"Device: Raspberry Pi, Classification: {classify_device(Device('Raspberry Pi', 1.5, 8, 16))}")
