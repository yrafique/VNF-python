import networkx as nx

class Topology:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node_id, attributes):
        self.graph.add_node(node_id, **attributes)

    def remove_node(self, node_id):import networkx as nx
    
    class Topology:
        def __init__(self):
            self.graph = nx.Graph()
    
        def add_node(self, node_id, attributes):
            self.graph.add_node(node_id, **attributes)
    
        def remove_node(self, node_id):
            self.graph.remove_node(node_id)
    
        def add_edge(self, node1, node2, attributes):
            self.graph.add_edge(node1, node2, **attributes)
    
        def remove_edge(self, node1, node2):
            self.graph.remove_edge(node1, node2)
    
        def update_node(self, node_id, attributes):
            for attr, value in attributes.items():
                self.graph.nodes[node_id][attr] = value
    
        def update_edge(self, node1, node2, attributes):
            for attr, value in attributes.items():
                self.graph[node1][node2][attr] = value
    
    
    
        self.graph.remove_node(node_id)

    def add_edge(self, node1, node2, attributes):
        self.graph.add_edge(node1, node2, **attributes)

    def remove_edge(self, node1, node2):
        self.graph.remove_edge(node1, node2)

    def update_node(self, node_id, attributes):
        for attr, value in attributes.items():
            self.graph.nodes[node_id][attr] = value

    def update_edge(self, node1, node2, attributes):
        for attr, value in attributes.items():
            self.graph[node1][node2][attr] = value
