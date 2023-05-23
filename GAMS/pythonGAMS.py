import os
import xml.etree.ElementTree as ET
import random

import subprocess
gams_path = "C:\GAMS\win64\24.9\gamside.exe"
subprocess.run([gams_path, "your_gams_file.gms"])

from gams import *

# Configuration
NoOfK = 3
NoOfVNFs = 5
NoOfApps = 1
LinkBWCap = 10000
UtilizationCap = 80
NoofUsers = 2
HostUtilizationCap = 80



os.environ['PATH'] = '/Applications/GAMS/gams24.9_osx_x64_64_sfx:' + os.environ['PATH']

# Read network instance (use newyork / abilene)
XML = ET.parse('Instances/newyork.xml').getroot()
XML = XML.find('networkStructure')

# Read Nodes from XML network instance
NoOfNodes = len(XML.find('nodes'))
NodeNames = []
Nodes = []
Nodes_x_pos = []
Nodes_y_pos = []
for i in range(NoOfNodes):
    node = XML.find('nodes').findall('node')[i]
    Nodes.append({
        'id': node.get('id'), 
        'x': float(node.find('coordinates').find('x').text),
        'y': float(node.find('coordinates').find('y').text),
        'CPU': 0,
        'users': []
    })
    Nodes_x_pos.append(Nodes[i]['x'])
    Nodes_y_pos.append(Nodes[i]['y'])
    NodeNames.append(Nodes[i]['id'])

# Read links from XML network instance
NoOfLinks = len(XML.find('links'))
LinkCost = [0 for _ in range(NoOfLinks)]
LinkCap = [0 for _ in range(NoOfLinks)]
# Build a bi-directional graph topology if it does not exist.
Topo = [[0 for _ in range(NoOfNodes)] for _ in range(NoOfNodes)]
GAMS_Topology = {'uels': [[0 for _ in range(NoOfNodes)] for _ in range(NoOfNodes)]}
for i in range(NoOfLinks):
    link = XML.find('links').findall('link')[i]
    s = NodeNames.index(link.find('source').text)
    d = NodeNames.index(link.find('target').text)
    Topo[s][d] = 1
    attributes = link.find('additionalModules').findall('addModule')
    if len(attributes) > 1:
        LinkCost[i] = float(attributes[1].find('cost').text)
        LinkCap[i] = float(attributes[1].find('capacity').text)
    else:
        LinkCost[i] = float(attributes.find('cost').text)
        LinkCap[i] = float(attributes.find('capacity').text)
    Topo[d][s] = 1



import random
from gams import *

# Generate random VNF requirements based on input parameter: NoOfVNFs
# VNF Properties (n= name, c= CPURequirement, pd = ProcessingDelay, dep = 0):

# Construct Set of VNFs
GAMS_VNFs = {'name': 'VNFs', 'uels': []}
VNF_Names = ['VNF' + str(i+1) for i in range(NoOfVNFs)]
VNF_CPUs = [0 for _ in range(NoOfVNFs)]
VNF_ProcDelays = [0 for _ in range(NoOfVNFs)]
VNF_Deps = [0 for _ in range(NoOfVNFs)]

for i in range(NoOfVNFs):
    VNF_CPUs[i] = round(random.uniform(1, 10), 2)
    VNF_ProcDelays[i] = round(random.uniform(1, 10), 2)
    VNF_Deps[i] = 0
    GAMS_VNFs['uels'].append([VNF_Names[i], VNF_CPUs[i], VNF_ProcDelays[i], VNF_Deps[i]])

# Generate random application requirements based on input parameter: NoOfApps

# Application Properties (n= name, vnf= number of VNFs, vnfs= list of VNFs, d= 0):

# Construct Set of Applications

GAMS_Apps = {'name': 'Apps', 'uels': []}
App_Names = ['App' + str(i+1) for i in range(NoOfApps)]
App_VNFs = [random.randint(2, NoOfVNFs) for _ in range(NoOfApps)]
App_VNF_Lists = []
App_Deps = [0 for _ in range(NoOfApps)]

for i in range(NoOfApps):
    App_VNF_Lists.append([random.choice(VNF_Names) for _ in range(App_VNFs[i])])
    GAMS_Apps['uels'].append([App_Names[i], App_VNFs[i], App_VNF_Lists[i], App_Deps[i]])

# Generate random user requirements based on input parameter: NoOfUsers

# User Properties (n= name, a= application, d= delay, r= rate):

# Construct Set of Users

GAMS_Users = {'name': 'Users', 'uels': []}
User_Names = ['User' + str(i+1) for i in range(NoOfUsers)]
User_Apps = [random.choice(App_Names) for _ in range(NoOfUsers)]
User_Delays = [round(random.uniform(1, 10), 2) for _ in range(NoOfUsers)]
User_Rates = [round(random.uniform(1, 10), 2) for _ in range(NoOfUsers)]

for i in range(NoOfUsers):
    GAMS_Users['uels'].append([User_Names[i], User_Apps[i], User_Delays[i], User_Rates[i]])

#Create GAMS Model

model = Model('NFV-VNE')

#Create GAMS Sets

Nodes_set = model.set('Nodes', range(NoOfNodes))
Links_set = model.set('Links', range(NoOfLinks))
VNFs_set = model.set('VNFs', range(NoOfVNFs))
Apps_set = model.set('Apps', range(NoOfApps))
Users_set = model.set('Users', range(NoofUsers))

#Create GAMS Parameters

#Link Parameters

LinkBW = model.param('LinkBW', LinkBWCap)
LinkCost = model.param('LinkCost', LinkCost)
LinkUtilization = model.param('LinkUtilization', UtilizationCap)

#Host Parameters

HostCapacity = model.param('HostCapacity', HostUtilizationCap)

#VNF Parameters

VNF_CPU = model.param('VNF_CPU', VNF_CPU)
VNF_PD = model.param('VNF_PD', VNF_PD)
VNF_Dep = model.param('VNF_Dep', VNF_Dep)

#Application Parameters

App_VNF = model.param('App_VNF', App_VNF)
App_BW = model.param('App_BW', App_BW)

#Create GAMS Variables

#Decision Variables

VNF_Placement = model.var('VNF_Placement', VNFs_set, Nodes_set, within=Binary)
VNF_Chaining = model.var('VNF_Chaining', VNFs_set, VNFs_set, within=Binary)
User_Assignment = model.var('User_Assignment', Users_set, Nodes_set, within=Binary)
Link_Utilization = model.var('Link_Utilization', Links_set, within=NonNegativeReals)
Host_Utilization = model.var('Host_Utilization', Nodes_set, within=NonNegativeReals)

#Create GAMS Constraints

#VNF Placement Constraints

model.equation(VNF_Placement.sum(VNFs_set) <= 1)
model.equation(VNF_Placement.sum(Nodes_set) <= 1)

#VNF Chaining Constraints

model.equation(VNF_Chaining.sum(VNFs_set) <= 1)
model.equation(VNF_Chaining.sum(VNFs_set) <= 1)

#User Assignment Constraints

model.equation(User_Assignment.sum(Users_set) <= 1)
model.equation(User_Assignment.sum(Nodes_set) <= 1)

#Link Utilization Constraints

model.equation(Link_Utilization.sum(Links_set) <= LinkBW)
model.equation(Link_Utilization.sum(Links_set) <= LinkUtilization)

#Host Utilization Constraints

model.equation(Host_Utilization.sum(Nodes_set) <= HostCapacity)

#Create GAMS Objective

#Objective Function

model.objective('minimize', LinkCost.sum(Links_set) + VNF_CPU.sum(VNFs_set))

#Solve GAMS Model

model.solve()

#Print Solution

print(VNF_Placement.get_values())
print(VNF_Chaining.get_values())
print(User_Assignment.get_values())
print(Link_Utilization.get_values())
print(Host_Utilization.get_Apps())
Users_set = model.set('Users', range(NoofUsers))

#Create GAMS Parameters

#Link Parameters

LinkBW = model.param('LinkBW', LinkBWCap)
LinkCost = model.param('LinkCost', LinkCost)
LinkUtilization = model.param('LinkUtilization', UtilizationCap)

#Host Parameters

HostCapacity = model.param('HostCapacity', HostUtilizationCap)

#VNF Parameters

VNF_CPU = model.param('VNF_CPU', VNF_CPU)
VNF_PD = model.param('VNF_PD', VNF_PD)
VNF_Dep = model.param('VNF_Dep', VNF_Dep)

#Application Parameters

App_VNF = model.param('App_VNF', App_VNF)
App_BW = model.param('App_BW', App_BW)

print(options.get_values())

#Finally, solve the model

model.solve()

#Print the objective value

print(model.get_objective_value())

#End of the code