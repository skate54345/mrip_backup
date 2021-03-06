import random
import socket
import threading
import time
import sys

initial_time = 30
starting_node = sys.argv[1]

def main():
    config_lines = getConfig("config.txt")
    i=0
    print("starting...\n")
    current_node = sys.argv[1]
    while True:
        #waits 30+R
        wait_time = 30+getInterval()
        time.sleep(wait_time)

        if(i<8):
            nodes = config_lines[i].split()
        else:
            i=0
            break
        #start with user input
        sender_ip = current_node
        #set destination to next neighbor
        destination_ip = getNeighbors(current_node)[1]
        print(">>>>>>>>>>>>>>>>>>>>>>>>")
        print("source:  "+sender_ip)
        print("dest:    "+destination_ip)
        print("cost:    1")
        request_message = "MRIP REQUEST " + sender_ip
        #update current node (starting_node) to next step
        current_node = destination_ip
        i+=1
        #constantly sends requests
        sendRequest(sender_ip, destination_ip, request_message)
        print("wait time: %s secs" % (wait_time))
        print(">>>>>>>>>>>>>>>>>>>>>>>>\n")

        print("<<<<<<<<<<<<<<<<<<<<<<<<")
        sendRouteMessage(sender_ip, i, destination_ip, getNeighbors(current_node)[1])
        print("<<<<<<<<<<<<<<<<<<<<<<<<\n")

#functions
def getConfig(f):
    file=open(f,"r")
    lines = [line.rstrip('\n') for line in file]
    return lines

#bellman ford
def getNeighbors(starting_node):
    pair_list = []
    i = 0
    lines = getConfig("config.txt")
    nodes = lines[i].split()
    for nodes in lines:
        nodes.rstrip(' ')
        if(starting_node in nodes):
            pair_list.append(nodes)
    #remove current node from pair and grab neighbor
    neighbor_list = [i.replace(starting_node, '').strip() for i in pair_list]
    #print("neighbors: ")
    #print(neighbor_list)
    return neighbor_list


def getInterval():
    R = random.randint(0,30)
    return R

def sendRequest(sender_ip, destination_ip, request_message):
    #UDP sending
    UDP_IP = destination_ip
    UDP_PORT = 5353 #must be 5353
    MESSAGE = request_message

    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT
    print "message: ", MESSAGE

    sock = socket.socket(socket.AF_INET, #internet
                          socket.SOCK_DGRAM) #UDPs
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

def sendRouteMessage(sender_ip, num, destination_ip, next_neighbor):
    print("message: ")
    print("MRIP ROUTE %s %s\n%s 1 %s" % (sender_ip, num, destination_ip, next_neighbor))

def startServer():
    UDP_IP = "10.0.0.0"
    UDP_PORT = 5353

    sock = socket.socket(socket.AF_INET, #internet
                         socket.SOCK_DGRAM) #UDP
    sock.bind((UDP_IP, UDP_PORT))

    #listen for requests
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print "received message: ", data

        getNeighbors(starting_node)

main()
