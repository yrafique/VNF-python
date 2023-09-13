# File Name: application.py
# This file defines the Application class, which represents an application composed of multiple microservices.

from microservice import Microservice  # Import Microservice class

class Application:
    def __init__(self, name):
        self.name = name  # Name of the application
        self.microservices = []  # List to hold microservices

    def add_microservice(self, microservice):
        self.microservices.append(microservice)

# Test function for Application class
def test_application():
    app1 = Application("Traffic Monitoring")
    ms1 = Microservice("Traffic Data Processing", "Traffic Monitoring", 2, 4, "AWS-EC2")
    app1.add_microservice(ms1)
    print(f"Application Name: {app1.name}, Microservices: {[ms.name for ms in app1.microservices]}")

# Sample print output: Application Name: Traffic Monitoring, Microservices: ['Traffic Data Processing']
