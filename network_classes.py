# This is network_classes.py
# Here we define all network-related classes used to represent different components of a network.

class Node:
    """
    Represents a node in the network. Nodes are basic units of the network structure,
    representing endpoints like routers, switches, servers, or clients.

    Attributes:
        uid (str): Unique identifier for the node.
        x (float): The x-coordinate of the node in the network diagram.
        y (float): The y-coordinate of the node in the network diagram.
    """
    def __init__(self, uid, x, y):
        self.uid = uid
        self.x = x
        self.y = y


class Link:
    """
    Represents a link between two nodes in the network. Links are used to connect nodes
    and represent physical or virtual network connections like cables, wireless paths, etc.

    Attributes:
        uid (str): Unique identifier for the link.
        source (str): UID of the source node for the link.
        target (str): UID of the target node for the link.
        capacity (float): The data capacity of the link (e.g., in Mbps).
        cost (float): The cost associated with using the link for data transmission.
        latency (float): The latency or delay (e.g., in ms) for data to travel across the link.
    """
    def __init__(self, uid, source, target, capacity, cost, medium='fiber'):  # Added 'medium' with default 'fiber'        self.uid = uid
        self.uid = uid
        self.source = source
        self.target = target
        self.capacity = capacity
        self.cost = cost
        self.medium = medium


class Demand:
    """
    Represents a network demand from one node to another. This could represent data traffic
    demands in a network simulation or real-world application.

    Attributes:
        uid (str): Unique identifier for the demand.
        source (str): UID of the source node generating the demand.
        destination (str): UID of the destination node for the demand.
        demandValue (float): The amount of data demand from source to destination (e.g., in Mbps).
    """
    def __init__(self, uid, source, destination, demandValue):
        self.uid = uid
        self.source = source
        self.destination = destination
        self.demandValue = demandValue


class Server:
    """
    Represents a server in the network, which could be a physical server, a virtual machine,
    or any computing resource capable of providing data and services to clients.

    Attributes:
        name (str): The name or model of the server.
        formFactor (int): The physical or virtual form factor of the server.
        architecture (str): The CPU architecture type of the server (e.g., x86, ARM).
        cpu (str): The CPU specifications, typically indicating speed and core count.
        memory (str): The memory capacity of the server, typically specified in GB or TB.
        storage (str): The data storage capacity of the server, typically specified in TB.
        source (str): Identifier for the server's data source or model.
        server_cost (float): The cost or price of the server, typically in units of currency.
    """
    def __init__(self, name, formFactor=None, architecture='N/A', cpu='N/A', memory='N/A', storage='N/A', source='N/A', server_cost=0.0):
        self.name = name
        self.formFactor = formFactor
        self.architecture = architecture
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.source = source
        self.server_cost = server_cost


class User:
    """
    Represents a user or client device in the network. This could be a personal computer,
    mobile device, IoT device, or any end-user device accessing network resources.

    Attributes:
        id (str): Identifier for the user or user device.
        pos (tuple): The (x, y) coordinates of the user device within the network.
        associated_ap (str): The Access Point the user is currently connected to.
        application (Application): The application assigned to the user, defining the services being used.
        measured_bw (float): The bandwidth measured or required for the user.
        measured_delay (float): The network delay measured or experienced by the user.
        associated_app (str): Identifier for the application associated with the user.
    """
    def __init__(self, user_id, pos, associated_ap):
        self.id = user_id
        self.pos = pos
        self.associated_ap = associated_ap
        self.application = None
        self.measured_bw = 0.0
        self.measured_delay = 0.0
        self.associated_app = None

    def assign_application(self, application):
        """
        Assigns an application to the user, linking the user's network activity with the specific application services.

        Args:
            application (Application): The application to assign to the user.
        """
        self.application = application
        self.associated_app = application.name
        self.measured_bw = application.bandwidth
        self.measured_delay = application.latency


class CNF:
    """
    Represents a Cloud-Native Function (CNF), which could be a Virtual Network Function (VNF),
    microservice, or any modular service component within a network application.

    Attributes:
        name (str): The name or identifier of the CNF.
        cpu (str): CPU requirement for the CNF, typically specified in GHz or cores.
        memory (str): Memory requirement for the CNF, typically specified in GB.
        storage (str): Storage requirement for the CNF, typically specified in GB.
        type (str): The type or category of the CNF (e.g., 'Network', 'Analytics', 'Security').
    """
    def __init__(self, name, cpu, memory, storage, type=None):
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.type = type


class Application:
    """
    Represents an application consisting of multiple CNFs (Cloud-Native Functions) in the network.
    This could represent a composite service such as a web application, IoT service, or network function.

    Attributes:
        name (str): The name or identifier of the application.
        bandwidth (float): The network bandwidth required by the application (e.g., in Mbps).
        latency (float): The network latency requirements of the application (e.g., in ms).
        device_density (int): The number of devices utilizing the application per unit area (e.g., devices/km²).
        source (str): The source of the application's requirements or configuration data.
        sfc (list): A list representing the Service Function Chain - the sequence of CNFs required by the application.
        users (list): A list of users or devices utilizing this application.
        cnfs (list): A list of CNFs that make up this application.
    """
    def __init__(self, name, bandwidth, latency, device_density, source, sfc):
        self.name = name
        self.bandwidth = bandwidth
        self.latency = latency
        self.device_density = device_density
        self.source = source
        self.sfc = sfc
        self.users = []
        self.cnfs = []

    def add_user(self, user):
        """
        Adds a user to this application's list of active users and assigns the application to that user.

        Args:
            user (User): The user to be added and assigned the application.
        """
        self.users.append(user)
        user.assign_application(self)

    def add_cnf(self, cnf):
        """
        Adds a Cloud-Native Function to this application's list of components.

        Args:
            cnf (CNF): The CNF to be added to the application.
        """
        self.cnfs.append(cnf)
