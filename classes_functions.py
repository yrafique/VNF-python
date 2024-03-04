# main.py

from prettytable import PrettyTable
import json

def update_node_attributes(G, node_name, **attrs):
    """Update attributes for a specific node."""
    for attr, value in attrs.items():
        G.nodes[node_name][attr] = value

def update_edge_attributes(G, source, destination, **attrs):
    """Update attributes for a specific edge."""
    for attr, value in attrs.items():
        G.edges[source, destination][attr] = value

def print_network_info(G):
    """Print detailed information about the network."""
    print("Servers (Nodes):")
    for node, attrs in G.nodes(data=True):
        print(f"{node}: {attrs}")
    print("\nLinks (Edges):")
    for source, destination, attrs in G.edges(data=True):
        print(f"{source} <-> {destination}: {attrs}")

def add_cnf_to_application(app, cnf_data, cnf_type):
    cnf = CNF(cnf_data.get('name', 'Unknown CNF'), cnf_data.get('storage', 'N/A'), cnf_data.get('memory', 'N/A'), cnf_data.get('cpu', 'N/A'))
    app.add_cnf(cnf, cnf_type)

def populate_applications(containers_data):
    applications = {}
    for container in containers_data:
        app_name = container.get('application', 'Unknown Application')
        app = Application(app_name, container.get('bandwidth', 'N/A'), container.get('latency', 'N/A'), container.get('device_density', 'N/A'), container.get('sfc', 'N/A'))
        
        for cnf_data in container.get('vnfs', []) + container.get('microservices', []):
            cnf_type = 'vnf' if cnf_data in container.get('vnfs', []) else 'microservice'
            add_cnf_to_application(app, cnf_data, cnf_type)
        
        applications[app_name] = app
    return applications

def populate_servers(G):
    servers = {}
    for node, attrs in G.nodes(data=True):
        server = Server(node, attrs.get('cpu', 'N/A'), attrs.get('memory', 'N/A'), attrs.get('storage', 'N/A'))
        servers[node] = server
    return servers

def populate_links(G):
    links = []
    for u, v, attrs in G.edges(data=True):
        link = Link(u, v, attrs.get('capacity', 'N/A'), attrs.get('cost', 'N/A'), attrs.get('latency', 'N/A'))
        links.append(link)
    return links

def populate_users(G_users):
    users = {}
    for user, attrs in G_users.nodes(data=True):
        user_obj = User(user, attrs.get('associated_ap', 'N/A'), attrs.get('application', 'N/A'), attrs.get('bandwidth', 'N/A'), attrs.get('latency', 'N/A'))
        users[user] = user_obj
    return users

def orchestrate_all(G, G_users, containers_data, output_file_path):
    servers = populate_servers(G)
    links = populate_links(G)
    users = populate_users(G_users)
    applications = populate_applications(containers_data)
    
    # Example function calls to print/save data (not fully implemented here)
    print("Servers, links, users, and applications have been populated.")

# Example execution block
if __name__ == "__main__":
    # Load JSON data
    with open("Devices\containers.json", "r") as json_file:
        containers_data = json.load(json_file)

    output_file_path = "complete_network_mapping.txt"
    
    # Mock data for G and G_users, assuming they're network graphs (e.g., from networkx library)
    # G = some_network_graph
    # G_users = some_user_graph
    orchestrate_all(G, G_users, containers_data, output_file_path)
    
    print("Note: Actual network graphs (G, G_users) need to be defined for the complete execution.")



    from prettytable import PrettyTable

def generate_sorted_cnf_user_summary(containers_data, app_to_users):
    # Initialize a dictionary to hold CNF details and associated user count
    cnf_details = {}

    # Loop through each container (application) to gather CNF and user details
    for container in containers_data['Containers']:
        app_name = container['application']
        users = app_to_users.get(app_name, [])  # Get users associated with this application
        
        # Process both Network Functions (vnfs) and Analytics Functions (microservices)
        for cnf_type, cnf_list in [('Network Function', container.get('vnfs', [])), 
                                   ('Analytics Function', container.get('microservices', []))]:
            for cnf in cnf_list:
                cnf_name = cnf['name']
                # Key to uniquely identify CNFs by name and type
                cnf_key = (cnf_name, cnf_type)
                
                # Initialize or update the CNF entry in the dictionary
                if cnf_key not in cnf_details:
                    cnf_details[cnf_key] = {'applications': set(), 'users': set()}
                cnf_details[cnf_key]['applications'].add(app_name)
                cnf_details[cnf_key]['users'].update(users)
                
    # Sort CNF entries by the count of associated users in descending order
    sorted_cnfs = sorted(cnf_details.items(), key=lambda item: len(item[1]['users']), reverse=True)
    
    # Create the summary table
    summary_table = PrettyTable(["CNF ID", "CNF Name", "CNF Type", "Applications", "Associated Users", "User Count"])
    cnf_id = 1
    for (cnf_name, cnf_type), details in sorted_cnfs:
        applications_str = ', '.join(sorted(details['applications']))
        users_str = ', '.join(sorted([str(user.split('_')[-1]) for user in details['users']]))
        user_count = len(details['users'])
        summary_table.add_row([cnf_id, cnf_name, cnf_type, applications_str, users_str, user_count])
        cnf_id += 1
    
    print(summary_table)

# Assuming `containers_data` and `app_to_users` are correctly populated
# Correctly call the function with your actual data
# generate_sorted_cnf_user_summary(containers_data, app_to_users)

