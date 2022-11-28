import sys
import xml.dom.minidom as dom 
import string
from xml.dom import minidom
from xml.dom.minidom import parse
import os

from pprint import pprint # to print element properties

#Read XML file
#network_name = "janos-us.xml"


#Create a Node class
class Node:
    def __init__(self,uid,x,y):
        self.uid=uid
        self.x=x
        self.y=y
        self.linklist=[]
        self.demandlist=[]

#Create a Link class
class Link:
    def __init__(self,uid,source,target,capacity,cost):
        self.uid=uid
        self.source=source
        self.target=target
        self.capacity=capacity
        self.cost = cost

#Create a Demand class
class Demand:
    def __init__(self,uid,source,destination,demandValue):
        self.uid=uid
        self.source=source
        self.destination=destination
        self.demandValue=demandValue


#Read Nodes from XML
def read_nodes(nodelist) -> dict:
    nodes = {} #creates empty nodes dictionary
    count_nodes = 0
    for node in nodelist :
        cur_node = {} #create temp node dictionary
        if node.hasAttribute("id"):
            Nodeid = node.getAttribute("id")
        x_cor = node.getElementsByTagName('x') [0] #Get dom object from XML
        x_cor = float(x_cor.childNodes[0].data) #Convert object to float
        y_cor = node.getElementsByTagName('y') [0] #Get dom object from XML
        y_cor = float(y_cor.childNodes[0].data) #Convert object to float
        cur_node = { 'id':Nodeid, 'x_cor':x_cor, 'y_cor':y_cor} #save into temp dict
        count_nodes +=1 #move to next node
        nodes[count_nodes] = cur_node #insert temp dict into nodes dict
    #print(nodes.keys()) #Print Level1 Dictionary Indexs
    #print(nodes) #Print Level1&2 Dictionary Values
    return nodes



#Read Links from XML
def read_links(linklist) -> dict:
    links = {}
    count_links = 0
    for link in linklist :
        cur_link = {} #create temp link dictionary
        if link.hasAttribute("id"):
            Linkid = link.getAttribute("id")
        Source = (link.getElementsByTagName('source') [0]).childNodes[0].data #Get dom object from XML
        Destination = (link.getElementsByTagName('target') [0]).childNodes[0].data
        Capacity = float((link.getElementsByTagName('capacity') [0]).childNodes[0].data)
        Cost = float((link.getElementsByTagName('cost') [0]).childNodes[0].data)
        cur_link = { 'source':Source, 'destination':Destination, 'capacity':Capacity, 'cost':Cost} #save into temp dict
        count_links +=1
        links[count_links] = cur_link
    #print(links.keys())
    #print(links)
    return links


#Read Demands from XML
def read_demands(demandlist)-> dict:
    demands = {}
    count_demands = 0
    for demand in demandlist :
        cur_demand = {} #create temp link dictionary
        if demand.hasAttribute("id"):
            Demandid = demand.getAttribute("id")
        Source = (demand.getElementsByTagName('source') [0]).childNodes[0].data #Get dom object from XML
        Destination = (demand.getElementsByTagName('target') [0]).childNodes[0].data
        Demandval = float((demand.getElementsByTagName('demandValue') [0]).childNodes[0].data)
        cur_demand = { 'source':Source, 'destination':Destination, 'demandValue':Demandval} #save into temp dict
        count_demands +=1
        demands[count_demands] = cur_demand
    return demands

#Function that will be called to read networks from other files
def read_network(filename: str) -> dict:
    Read_Data = minidom.parse(filename)
    nodelist = Read_Data.getElementsByTagName("node")
    nodes = read_nodes(nodelist)

    linklist = Read_Data.getElementsByTagName("link")
    links = read_links(linklist)

    demandlist = Read_Data.getElementsByTagName("demand")
    demands = read_demands(demandlist)

    c = nodes, links, demands

    return c


#Print Read File
#Testing Nodes
def print_test(network_name: str, nodes: dict, links: dict, demands: dict ):
    print('\n\nNetwork Name: ' + network_name)

    print('\n**** Nodes read: ******\n')
    for node in nodes:
        s = 'Node # \t' + str(node) + ': \t' + (nodes.get(node).get("id")).ljust(20) + '\tx: ' + str(nodes.get(node).get("x_cor")) + ', \ty: '+ str(nodes.get(node).get("y_cor")) 
        #s = 'Node # \t' + str(node) + ': \t' + nodes.get(node).get("id") + '\tx: ' + str(nodes.get(node).get("x_cor")) + ', \ty: '+ str(nodes.get(node).get("y_cor")) 
        print(s)

    print('\n**** Links read: ******\n')
    for link in links:
        s = 'Link # \t' + str(link) + ', From: ' + (links.get(link).get("source")).ljust(15) + ', To: '+ (links.get(link).get("destination")).ljust(15)+ ",\t Capacity: " + str(links.get(link).get("capacity")) + ", \tCost: " + str(links.get(link).get("cost"))
        print(s)
