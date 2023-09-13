# File Name: run_simulation.py
# This file runs all the test functions for the classes to simulate the entire workflow.

from server import test_server  # Import the test function for Server
from microservice import test_microservice  # Import the test function for Microservice
from link import test_link  # Import the test function for Link
from application import test_application  # Import the test function for Application
from cost_calculation import test_calculate_cost  # Import the test function for Cost Calculation
from server_selection import test_select_server  # Import the test function for Server Selection
from bandwidth_calculation import test_calculate_bandwidth  # Import the test function for Bandwidth Calculation

if __name__ == "__main__":
    print("Running all tests...\n")
    
    print("1. Running Server Test:")
    test_server()
    
    print("\n2. Running Microservice Test:")
    test_microservice()
    
    print("\n3. Running Link Test:")
    test_link()
    
    print("\n4. Running Application Test:")
    test_application()
    
    print("\n5. Running Cost Calculation Test:")
    test_calculate_cost()
    
    print("\n6. Running Server Selection Test:")
    test_select_server()
    
    print("\n7. Running Bandwidth Calculation Test:")
    test_calculate_bandwidth()
    
    print("\nAll tests completed.")
