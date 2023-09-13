# File Name: link.py
# This file defines the Link class, which represents a network link between servers.

class Link:
    def __init__(self, id, bandwidth, latency):
        self.id = id  # Unique identifier for the link
        self.bandwidth = bandwidth  # Link bandwidth in Gbps
        self.latency = latency  # Latency in ms

# Test function for Link class
def test_link():
    link1 = Link("Link1", 10, 5)
    print(f"Link ID: {link1.id}, Bandwidth: {link1.bandwidth} Gbps, Latency: {link1.latency} ms")

# Sample print output: Link ID: Link1, Bandwidth: 10 Gbps, Latency: 5 ms
