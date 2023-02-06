import networkx as nx
import random

class User:
    def __init__(self, x, y, app_req):
        self.x = x
        self.y = y
        self.app_req = app_req

class Demand:
    def __init__(self, src, dest, bw, delay):
        self.src = src
        self.dest = dest
        self.bw = bw
        self.delay = delay

class App:
    def __init__(self, name, vnfs):
        self.name = name
        self.vnfs = vnfs

class Candidate:
    def __init__(self, name, x, y, cpu, storage):
        self.name = name
        self.x = x
        self.y = y
        self.cpu = cpu
        self.storage = storage
        self.cpu_used = 0
        self.storage_used = 0
        
    def place_vnf(self, vnf_cpu, vnf_storage):
        self.cpu_used += vnf_cpu
        self.storage_used += vnf_storage

# Create a graph to represent the network
G = nx.Graph()


# Add nodes to the graph (representing network devices)
for i in range(10):
    G.add_node(i, cpu=random.randint(1, 1000), storage=random.randint(1, 1000))
    nx.set_node_attributes(G, 0, 'cpu_used')
    nx.set_node_attributes(G, 0, 'storage_used')

# Add edges to the graph (representing network links)
for i in range(10):
    for j in range(i+1, 10):
        G.add_edge(i, j, bandwidth=random.randint(1, 100000), delay=random.randint(1, 10))

# Create a list of users
user_list = [User(random.randint(1, 10), random.randint(1, 10), "App1") for i in range(5)]

# Create a list of demands
demand_list = [Demand(random.randint(0, 9), random.randint(0, 9), random.randint(1, 100), random.randint(1, 100)) for i in range(5)]

# Create a list of VNFs
vnf_list = [{'name': 'VNF1', 'cpu': random.randint(1, 10), 'storage': random.randint(1, 10)},
            {'name': 'VNF2', 'cpu': random.randint(1, 10), 'storage': random.randint(1, 10)},
            {'name': 'VNF3', 'cpu': random.randint(1, 10), 'storage': random.randint(1, 10)}]

# Select a random subset of vnf_list
subset_size = 3 # change this to the desired subset size
random_subset = random.sample(vnf_list, subset_size)

# Create an App object with the selected subset of VNFs
app = App("App1", random_subset)

# Select a random candidate node for VNF placement
candidate = random.choice([node for node in G.nodes()])

def VNF_Placement(G, user_list, demand_list, app_list, candidate):
    src = candidate
    dest = candidate
    path = nx.shortest_path(G, src, dest)
    cost = 0
    print('SFC Path:', path)

    if 'cpu' not in G.nodes[candidate] or 'storage' not in G.nodes[candidate]:
        print("Error: candidate node has no CPU or storage attributes.")
        return False
    cpu_avail = G.nodes[candidate]['cpu']
    storage_avail = G.nodes[candidate]['storage']
    for demand in demand_list:
        src = demand.src
        dest = demand.dest
        bw = demand.bw
        delay = demand.delay
        if not check_bandwidth(G, src, dest, bw) or not check_delay(G, src, dest, delay):
            print('Link Usage:', G.edges[u, v]['bandwidth'])
            return False
    for vnf in app_list.vnfs:
        if 'cpu' not in vnf or 'storage' not in vnf:
            print("Error: VNF is missing CPU or storage attributes.")
            return False
        cpu_req = vnf['cpu']
        storage_req = vnf['storage']
        if cpu_req > cpu_avail or storage_req > storage_avail:
            print("Error: not enough resources to place VNF on candidate node.")
            return False
        cpu_avail -= cpu_req
        storage_avail -= storage_req
        cost += 100  # added this line to increment cost after each VNF placement

    
    G.nodes[candidate]['cpu_used'] += sum([vnf['cpu'] for vnf in app_list.vnfs])
    print('VNF Resource Usage:', G.nodes[candidate]['cpu_used'])
    G.nodes[candidate]['storage_used'] += sum([vnf['storage'] for vnf in app_list.vnfs])

    cost = sum([G.edges[u, v]['cost'] for u, v in zip(path, path[1:])])
    print('Cost:', cost)


    #   print stats:
    for u, v in zip(path, path[1:]):
        print('Link Usage:', G.edges[u, v]['bandwidth'])
    for node in path:
        print('VNF Resource Usage:', G.nodes[node]['cpu_used'])
    
    return True

def check_bandwidth(G, src, dest, bw):
    path = nx.shortest_path(G, src, dest)
    for i in range(len(path) - 1):
        u = path[i]
        v = path[i + 1]
        if G.edges[u, v]['bandwidth'] < bw:
            print("Error: not enough bandwidth on edge ", u, " - ", v)
            return False
    return True



def check_delay(G, src, dest, delay):
    path = nx.shortest_path(G, src, dest)
    for i in range(len(path) - 1):
        u = path[i]
        v = path[i + 1]
        if G.edges[u, v]['delay'] > delay:
            print("Error: delay is more than expected on edge ", u, " - ", v)
            return False
    return True




# Test the VNF placement function
result = VNF_Placement(G, user_list, demand_list, app, candidate)
print("VNF Placement Successful" if result else "VNF Placement Failed")



