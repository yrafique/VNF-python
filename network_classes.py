# network_classes.py
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
        """Initialize a new Node instance."""
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
        propagation_delay (float): The latency (e.g., in ms) based on the propagation delay.
    """
    def __init__(self, uid, source, target, capacity, cost, propagation_delay=0):
        """Initialize a new Link instance."""
        self.uid = uid
        self.source = source
        self.target = target
        self.capacity = capacity
        self.cost = cost
        self.propagation_delay = propagation_delay

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
        """Initialize a new Demand instance."""
        self.uid = uid
        self.source = source
        self.destination = destination
        self.demandValue = demandValue
       
# class Server:
#     """
#         Represents a server in the network.

#         Attributes:
#             name (str): The name of the server model.
#             formFactor (int): The form factor of the server, typically a numerical value indicating size or capacity.
#             architecture (str): The CPU architecture type of the server, typically indicating the instruction set architecture such as x86 or ARM.
#             cpu (str): The CPU specification of the server, typically indicating speed and core count.
#             memory (str): The memory capacity of the server, typically specified in GB or TB.
#             storage (str): The storage capacity of the server, typically specified in TB.
#             source (str): The data source or the specific model identifier for the server.
#             server_cost (float): The cost or price of the server, typically in units of currency.
#     """
   
#     def __init__(self, name, formFactor, architecture, cpu, memory, storage, source, server_cost):
#         self.name = name
#         self.formFactor = formFactor
#         self.architecture = architecture
#         self.cpu = cpu
#         self.memory = memory
#         self.storage = storage
#         self.source = source
#         self.server_cost = server_cost
#         self.applications = []

#     def deploy_application(self, application):
#         # Check if resources are sufficient
#         if self.cpu >= application.total_cpu and self.memory >= application.total_memory and self.storage >= application.total_storage:
#             self.cpu -= application.total_cpu
#             self.memory -= application.total_memory
#             self.storage -= application.total_storage
#             self.applications.append(application)
#             return True
#         return False

#     def remove_application(self, application_name):
#         self.applications = [app for app in self.applications if app.name != application_name]

#     def __str__(self):
#         return f"Server {self.id}: CPU={self.cpu} GHz, Memory={self.memory} GB, Storage={self.storage} GB"
    


class Server:
    def __init__(self, name, cpu, memory, storage, formFactor=None, architecture=None, source=None, server_cost=0):
        self.name = name
        self.formFactor = formFactor
        self.architecture = architecture
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.source = source
        self.server_cost = server_cost
        self.applications = []

    def deploy_application(self, application):
        if self.cpu >= application.total_cpu and self.memory >= application.total_memory and self.storage >= application.total_storage:
            self.cpu -= application.total_cpu
            self.memory -= application.total_memory
            self.storage -= application.total_storage
            self.applications.append(application)
            return True
        return False

    def remove_application(self, application_name):
        app = next((app for app in self.applications if app.name == application_name), None)
        if app:
            self.cpu += app.total_cpu
            self.memory += app.total_memory
            self.storage += app.total_storage
            self.applications.remove(app)

    def __str__(self):
        return (f"Server({self.name}, CPU: {self.cpu} GHz, Memory: {self.memory} GB, "
                f"Storage: {self.storage} GB, Cost: {self.server_cost}$)")



class User:
    """
    Represents a user device in the network.

    Attributes:
        id (str): Identifier for the user.
        pos (tuple): The (x, y) coordinates of the user device.
        associated_ap (str): The Access Point the user is connected to.
        application (Application): The application assigned to the user. Initially None until assigned.
        measured_bw (float): The measured bandwidth for the user. Initially 0.0 and updated later.
        measured_delay (float): The measured delay for the user. Initially 0.0 and updated later.
        associated_app (str): The application associated with the user. Initially None until assigned.
    """
    def __init__(self, user_id, pos, associated_ap):
        """Initialize a new User instance."""
        self.id = user_id
        self.pos = pos
        self.associated_ap = associated_ap
        self.application = None
        self.measured_bw = 0.0
        self.measured_delay = 0.0
        self.associated_app = None
    
    def assign_application(self, application):
        """
        Assigns an application to the user and updates related attributes.

        Args:
            application (Application): The application to be assigned to the user.
        """
        self.application = application
        self.associated_app = application.name
        self.measured_bw = application.bandwidth
        self.measured_delay = application.latency

class CNF:
    """
    Represents a Cloud-Native Function (CNF) or a service component in the network.

    Attributes:
        name (str): The name of the CNF.
        cpu (float): CPU requirement for the CNF (e.g., in GHz).
        memory (float): Memory requirement for the CNF (e.g., in GB).
        storage (float): Storage requirement for the CNF (e.g., in GB).
        type (str): The type of CNF (e.g., 'Network', 'Analytics').
    """
    def __init__(self, name, cpu, memory, storage, type=None):
        """Initialize a new CNF instance."""
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.type = type

    def __str__(self):
        return f"Container {self.name}: CPU={self.cpu} GHz, Memory={self.memory} GB, Storage={self.storage} GB"

class Application:
    """
    Represents an application consisting of one or more CNFs in the network.
    
    Attributes:
        name (str): The name of the application.
        bandwidth (float): Average bandwidth required by the application (in Mbps).
        latency (float): Average latency requirements of the application (in ms).
        device_density (int): The density of devices utilizing the application (devices per square km).
        source (str): The source or origin of the application requirements or data.
        sfc (list): The Service Function Chain, representing the sequence of CNFs required by the application.
        users (list): The users that are using this application.
        cnfs (list): The CNFs that make up this application.
        total_cpu (float): Total CPU required by the application.
        total_memory (float): Total memory required.
        total_storage (float): Total storage required.
    """
    def __init__(self, name, bandwidth, latency, device_density, source, sfc=[], total_cpu=0, total_memory=0, total_storage=0):
        self.name = name
        self.bandwidth = np.mean(bandwidth) if isinstance(bandwidth, list) else bandwidth
        self.latency = np.mean(latency) if isinstance(latency, list) else latency
        self.device_density = device_density
        self.source = source
        self.sfc = sfc
        self.users = []
        self.cnfs = []
        self.total_cpu = total_cpu
        self.total_memory = total_memory
        self.total_storage = total_storage

    def add_user(self, user):
        """
        Adds a user to this application's user list and assigns this application to the user.

        Args:
            user (User): The user to add and assign the application to.
        """
        self.users.append(user)
        user.assign_application(self)

    def add_cnf(self, cnf):
        """
        Adds a Cloud-Native Function (CNF) to this application.

        Args:
            cnf (CNF): The CNF to add to the application.
        """
        self.cnfs.append(cnf)

    def __str__(self):
        return f"Application {self.name}: Bandwidth={self.bandwidth} Mbps, Latency={self.latency} ms"


