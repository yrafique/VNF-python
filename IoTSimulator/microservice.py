# File Name: microservice.py
# This file defines the Microservice class that contains attributes related to microservices.

class Microservice:
    def __init__(self, name, application, cpu_requirement, ram_requirement, server_type, latency_sensitivity, bandwidth_requirement):
        self.name = name
        self.application = application
        self.cpu_requirement = cpu_requirement
        self.ram_requirement = ram_requirement
        self.server_type = server_type
        self.latency_sensitivity = latency_sensitivity
        self.bandwidth_requirement = bandwidth_requirement

# Test function for Microservice class
def test_microservice():
    ms1 = Microservice("Traffic Data Processing", "Traffic Monitoring", 2, 4, "AWS-EC2", 0.2, 0.5)
    print(f"Microservice: {ms1.name}, Application: {ms1.application}, CPU Requirement: {ms1.cpu_requirement} cores, RAM Requirement: {ms1.ram_requirement} GB, Server Type: {ms1.server_type}, Latency Sensitivity: {ms1.latency_sensitivity}, Bandwidth Requirement: {ms1.bandwidth_requirement} Gbps.")

# Sample print output from test function
# Microservice: Traffic Data Processing, Application: Traffic Monitoring, CPU Requirement: 2 cores, RAM Requirement: 4 GB, Server Type: AWS-EC2, Latency Sensitivity: 0.2, Bandwidth Requirement: 0.5 Gbps

if __name__ == "__main__":
    test_microservice()
