# Filename: server_selection.py
# Description: This file contains the code for optimizing server selection based on different algorithms.

from cost_calculation import calculate_cost
from cost_calculation import ServerCost
from microservice_allocation import Microservice

# Greedy First-Come-First-Serve Algorithm
def greedy_fcfs(microservices, servers):
    """Optimize server selection using Greedy First-Come-First-Serve algorithm."""
    optimized_cost = {}
    for ms in microservices:
        min_cost = float('inf')
        best_server = None
        for server in servers:
            cost = ms.cpu * server.hourly_rate
            if cost < min_cost:
                min_cost = cost
                best_server = server.name
        optimized_cost[ms.name] = (best_server, min_cost)
    return optimized_cost

# PageRank Algorithm
def pagerank(microservices, servers):
    """Optimize server selection using PageRank algorithm."""
    # Implementation would include a sophisticated scoring method
    # For this example, we will use a simplified version
    optimized_cost = {}
    for ms in microservices:
        best_server = sorted(servers, key=lambda x: x.hourly_rate)[0].name
        cost = ms.cpu * servers[0].hourly_rate
        optimized_cost[ms.name] = (best_server, cost)
    return optimized_cost

# Test function
def test_server_selection():
    """Test the server selection algorithms."""
    server1 = ServerCost("AWS-EC2", 0.05796)
    server2 = ServerCost("Azure-VM", 0.0835)
    
    ms1 = Microservice("Traffic Data Processing", "Traffic Monitoring", 2, 4, "AWS-EC2")
    ms2 = Microservice("Weather Data Analysis", "Weather Forecast", 1, 2, "Azure-VM")
    
    result = greedy_fcfs([ms1, ms2], [server1, server2])
    assert result == {'Traffic Data Processing': ('AWS-EC2', 0.11592), 'Weather Data Analysis': ('AWS-EC2', 0.05796)}
    
    result = pagerank([ms1, ms2], [server1, server2])
    assert result == {'Traffic Data Processing': ('AWS-EC2', 0.11592), 'Weather Data Analysis': ('AWS-EC2', 0.05796)}
    
    print("All tests passed!")

# Sample print statement
test_server_selection()
print(f"Optimized Server Selection using Greedy FCFS: {greedy_fcfs([Microservice('Traffic Data Processing', 'Traffic Monitoring', 2, 4, 'AWS-EC2'), Microservice('Weather Data Analysis', 'Weather Forecast', 1, 2, 'Azure-VM')], [ServerCost('AWS-EC2', 0.05796), ServerCost('Azure-VM', 0.0835)])}")

# Output of test function
# All tests passed!
# Optimized Server Selection using Greedy FCFS: {'Traffic Data Processing': ('AWS-EC2', 0.11592), 'Weather Data Analysis': ('AWS-EC2', 0.05796)}
