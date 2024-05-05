# classes.py
class Server:
    """Represents a server in the network."""
    def __init__(self, name, cpu='N/A', memory='N/A', storage='N/A'):
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.storage = storage

    def update_attributes(self, G, cpu=None, memory=None, storage=None):
        """Update server attributes and corresponding node in NetworkX graph."""
        if cpu: self.cpu = cpu
        if memory: self.memory = memory
        if storage: self.storage = storage
        G.nodes[self.name]['cpu'] = self.cpu
        G.nodes[self.name]['memory'] = self.memory
        G.nodes[self.name]['storage'] = self.storage

    def print_attributes(self):
        """Print server attributes."""
        print(f"Server {self.name}: CPU={self.cpu}, Memory={self.memory}, Storage={self.storage}")

class Link:
    """Represents a link between two nodes in the network."""
    def __init__(self, source, destination, capacity='N/A', cost='N/A', latency='N/A'):
        self.source = source
        self.destination = destination
        self.capacity = capacity
        self.cost = cost
        self.latency = latency

    def update_attributes(self, G, capacity=None, cost=None, latency=None):
        """Update link attributes and corresponding edge in NetworkX graph."""
        if capacity is not None: self.capacity = capacity
        if cost is not None: self.cost = cost
        if latency is not None: self.latency = latency
        # Update attributes in the graph
        G.edges[self.source, self.destination]['capacity'] = self.capacity
        G.edges[self.source, self.destination]['cost'] = self.cost
        G.edges[self.source, self.destination]['latency'] = self.latency

    def print_attributes(self):
        """Print link attributes."""
        print(f"Link from {self.source} to {self.destination}: Capacity={self.capacity}, Cost={self.cost}, Latency={self.latency}")


class User:
    """Represents a user in the network."""
    def __init__(self, name, associated_ap='N/A', application=None, bandwidth='N/A', latency='N/A'):
        self.name = name
        self.associated_ap = associated_ap
        self.application = application
        self.bandwidth = bandwidth
        self.latency = latency
        

class CNF:
    """Represents a Cloud Native Function."""
    def __init__(self, name, storage, memory, cpu, type):
        self.name = name
        self.storage = storage
        self.memory = memory
        self.cpu = cpu
        self.type = type

class Application:
    """Represents an application running on the network."""
    def __init__(self, name, bandwidth, latency, device_density, sfc):
        self.name = name
        self.bandwidth = bandwidth
        self.latency = latency
        self.device_density = device_density
        self.sfc = sfc #order of cnfs
        self.users = []  # List of associated users
        self.cnfs = {}  # Dictionary to store both VNFs and Microservices

    def add_user(self, user):
        """Add a user associated with this application."""
        self.users.append(user)
    
    def add_cnf(self, cnf, cnf_type):
        """Add a CNF (VNF or Microservice) to the application."""
        self.cnfs[cnf.name] = {'type': cnf_type, 'cnf': cnf}