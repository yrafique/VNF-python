# File Name: server.py
# This file defines the Server class that contains attributes related to server resources.

class Server:
    def __init__(self, server_type, cpu, ram, storage, bandwidth, latency):
        self.server_type = server_type
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.bandwidth = bandwidth
        self.latency = latency

# Test function for Server class
def test_server():
    server1 = Server("AWS-EC2", 8, 16, 200, 1, 10)
    print(f"Server: {server1.server_type}, CPU: {server1.cpu} cores, RAM: {server1.ram} GB, Storage: {server1.storage} GB, Bandwidth: {server1.bandwidth} Gbps, Latency: {server1.latency} ms.")

# Sample print output from test function
# Server: AWS-EC2, CPU: 8 cores, RAM: 16 GB, Storage: 200 GB, Bandwidth: 1 Gbps, Latency: 10 ms

if __name__ == "__main__":
    test_server()
