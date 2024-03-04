# This is network_classes.py
# Here we define all network-related classes used to represent different components of a network.

class Node:
    """
    Represents a node in the network.

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
    Represents a link between two nodes in the network.
    
    Attributes:
        uid (str): Unique identifier for the link.
        source (str): UID of the source node.
        target (str): UID of the target node.
        capacity (float): The capacity of the link (e.g., in Mbps).
        cost (float): The cost associated with using the link.
        latency (float): The latency (e.g., in ms) based on the propagation delay.
    """
    def __init__(self, uid, source, target, capacity, cost, propogation_delay=0):
        self.uid = uid
        self.source = source
        self.target = target
        self.capacity = capacity
        self.cost = cost
        self.propogation_delay = propogation_delay

class Demand:
    """
    Represents a demand from one node to another in the network.

    Attributes:
        uid (str): Unique identifier for the demand.
        source (str): UID of the source node.
        destination (str): UID of the destination node.
        demandValue (float): The amount of demand from source to destination (e.g., in Mbps).
    """
    def __init__(self, uid, source, destination, demandValue):
        self.uid = uid
        self.source = source
        self.destination = destination
        self.demandValue = demandValue

class Server:
    """
    Represents a server in the network.

    Attributes:
        name (str): The name of the server model.
        formFactor (int): The form factor of the server, typically a numerical value indicating size or capacity.
        architecture (str): The CPU architecture type of the server, typically indicating the instruction set architecture such as x86 or ARM.
        cpu (str): The CPU specification of the server, typically indicating speed and core count.
        memory (str): The memory capacity of the server, typically specified in GB or TB.
        storage (str): The storage capacity of the server, typically specified in TB.
        source (str): The data source or the specific model identifier for the server.
        server_cost (float): The cost or price of the server, typically in units of currency.
    """
    def __init__(self, name, formFactor=None, architecture='N/A', cpu='N/A', memory='N/A', storage='N/A', source='N/A', server_cost=0.0):
        """Initialize a new Server instance."""
        self.name = name
        self.formFactor = formFactor
        self.architecture = architecture
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.source = source
        self.server_cost = server_cost

    def update_attributes(self, **kwargs):
        """
        Update server attributes based on keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments representing server attributes.
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                print(f"Warning: {key} is not a valid attribute of Server.")

class User:
    """
    Represents a user device in the network.

    Attributes:
        id (str): Identifier for the user.
        pos (tuple): The (x, y) coordinates of the user device.
        associated_ap (str): The Access Point the user is connected to.
        application (Application): The application assigned to the user.
        measured_bw (float): The measured bandwidth for the user.
        measured_delay (float): The measured delay for the user.
        associated_app (str): The application associated with the user.
    """
    def __init__(self, user_id, pos, associated_ap):
        self.id = user_id
        self.pos = pos
        self.associated_ap = associated_ap
        self.application = None  # This will be set later
        self.measured_bw = 0.0  # Default bandwidth, can be updated later
        self.measured_delay = 0.0  # Default delay, can be updated later
        self.associated_app = None  # This will be set later
    
    def assign_application(self, application):
        """Assigns an application to the user."""
        self.application = application
        self.associated_app = application.name  # Assuming Application has a 'name' attribute
        # Set bandwidth and delay based on the application's requirements
        self.measured_bw = application.bandwidth  # Assuming Application has a 'bandwidth' attribute
        self.measured_delay = application.latency  # Assuming Application has a 'latency' attribute



class CNF:
    """
    Represents a Cloud-Native Function or service component.

    Attributes:
        name (str): The name of the CNF.
        storage (str): Storage requirement for the CNF (e.g., in GB).
        memory (str): Memory requirement for the CNF (e.g., in GB).
        cpu (str): CPU requirement for the CNF.
        type (str): The type of CNF (e.g., 'VNF', 'Microservice').
    """
    def __init__(self, name, cpu, memory, storage, type=None):
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.type = type  # Type can be 'Network', 'Analytics', or another classification.


# Define the classes
class Application:
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
        self.users.append(user)
        user.assign_application(self)

    def add_cnf(self, cnf):
        self.cnfs.append(cnf)



