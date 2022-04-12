from logging import NullHandler
from operator import irshift
from re import X
import scapy.all as scapy
import netifaces
import netaddr
import socket
import hashlib
import json

def getSubnet():
        ip = netifaces.ifaddresses('eth0')
        ipAddress = ip[netifaces.AF_INET][0].get("addr")
        netmask = ip[netifaces.AF_INET][0].get("netmask")
        bitmask = str(netaddr.IPAddress(netmask).netmask_bits())
        x = netaddr.IPNetwork(ipAddress + "/" + bitmask)
        network = str(x.network)
        return network + "/" + bitmask

def arpHostDescovery(ipRange):
        x, null = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst=ipRange),timeout=0.25,verbose=0) #Construcsts and sends an arp packet asking for ff:ff:ff:ff:ff:ff
        hostsOnNetwork = []
        for resNum in range(len(x.res)): #Gets number of hosts found from res
                hostsOnNetwork.append(x.res[resNum][0][scapy.ARP].pdst) #Adding the pdst(IP) for the hosts found to a list
        hostsOnNetwork.remove("192.168.1.1")
        hostsOnNetwork.remove("192.168.1.108")
        return hostsOnNetwork


def portScanner(hostsList):
        openPorts = {}
        for host in hostsList:
                print("scanning " + host)
                openPorts[host] = []
                for port in range(1, 65535):
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        result = sock.connect_ex((host, port))
                        if result == 0:
                                print("Port " + str(port) + "is open")
                                openPorts[host].append(port)
                                print(openPorts)
                        sock.close()
        return openPorts

def fingerPrinter(openPorts, hostsOnNetwork):
        fingerPrints = {}
        iterator = -1
        for host in hostsOnNetwork:
                iterator += 1
                fingerPrints[hostsOnNetwork[iterator]] = []
                for port in openPorts[host]:
                        sock = socket.socket()
                        try:
                                sock.connect((hostsOnNetwork[iterator], port))
                                data = sock.recv(1024)
                                fingerPrints[host].append(data)
                                sock.close()
                        except:
                                continue
                        print(data)
        formatFingerPrints = {}
        for hosts in hostsOnNetwork:
                fingerprint = hashlib.md5(str(openPorts[hosts]).encode() + str(fingerPrints[hosts]).encode())
                print (fingerprint.hexdigest())
                formatFingerPrints[hosts] = fingerprint.hexdigest()
        return formatFingerPrints


def readFromJson():
        with open("/home/scanner/IOTVulnrablityScanner/internal/IOTScanner/fingerprints.json", 'r') as fingerpints:
                data = json.load(fingerpints)
        return data

def webInteraction(jsonData, fingerprints):
    print(type(jsonData))
    vulnrableDevices = []
    for key in fingerprints:
        print(fingerprints[key])
        try:
            vulnrableDevices.append(jsonData[fingerprints[key]])
        except:
            print("Not in json file")
    return vulnrableDevices


def main():
    print("Calling getSubnet()")
    subnet = getSubnet()
    print("Given " + str(subnet))
    print("Calling arpHostDescovery(subnet)")
    hosts = arpHostDescovery(subnet)
    print("Given " + str(hosts))
    print("Calling portScanner(hosts)")
    ports = portScanner(hosts)
    print("Given " + str(ports))
    print("Calling fingerPrinter(ports, hosts)")
    fingerprints = fingerPrinter(ports, hosts)
    print("Given " + str(fingerprints))
    print("Calling readFromJson()")
    jsonData = readFromJson()
    print("Calling webInteration(jsonData, fingerprints)")
    webData = webInteraction(jsonData, fingerprints)
    return webData


"""
if __name__ == '__main__':
        print("Starting .... ")
        print("Calling GetSubnet")
        #currentSubent = getSubnet()
        print("Getting Hosts On Network")
        #hostsOnNetwork = arpHostDescovery(currentSubent)
       # portResults = portScanner(["192.168.1.2","192.168.1.108"])
        testData = {'192.168.1.2': [22, 38262, 44470], '192.168.1.157': [23, 554, 6668, 7101, 7103]}
        #fingerPrinter(testData, ["192.168.1.2","192.168.1.157"])
        x = ["192.168.1.2","192.168.1.157"]
        readFromJson()
        #print(hostsOnNetwork)
        #openPorts = {'192.168.1.2': [22, 38262, 44470], '192.168.1.157': [23, 554, 6668, 7101, 7103]}
       # fingerPrints = {'192.168.1.2': [b'SSH-2.0-OpenSSH_8.4p1 Debian-5\r\n'], '192.168.1.157': [b'\xff\xfd\x01\xff\xfd\x1f\xff\xfb\x01\xff\xfb\x03', b'', b'', b'', b'']}
       # formatFingerPrints = {}
      #  for hosts in x:
          #      fingerprint = hashlib.md5(str(openPorts[hosts]).encode() + str(fingerPrints[hosts]).encode())
       #         print (fingerprint.hexdigest())
          #      formatFingerPrints[hosts] = fingerprint.hexdigest()
       # print (formatFingerPrints)
"""                
        


"""
def testing():
    vulrnableDevices = [["Device Name", "Finger Print"] ,["Device Name","Finger Print"]]
    nullList =  [["Device Name", "Finger Print"] ,["Device Name","Finger Print"]]
    if len(nullList)==0:
        print("empty")
    else:
        print("Not empty")
    return vulrnableDevices
"""
