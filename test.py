def getSubnet():
        ip = netifaces.ifaddresses('eth0')
        ipAddress = ip[netifaces.AF_INET][0].get("addr")
        netmask = ip[netifaces.AF_INET][0].get("netmask")
        bitmask = str(netaddr.IPAddress(netmask).netmask_bits())
        x = netaddr.IPNetwork(ipAddress + "/" + bitmask)
        network = str(x.network)
        return network + "/" + bitmask


def arpHostDescovery(ipRange):
        x, null = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst=ipRange),timeout=0.25,verbose=0) #Construcsts and sends an Arp packet asking for ff:ff:ff:ff:ff:ff
        hostsOnNetwork = []
        for resNum in range(len(x.res)): #Gets number of hosts found from res
                hostsOnNetwork.append(x.res[resNum][0][scapy.ARP].pdst) #Adding the pdst(IP) for the hosts found to a list
        return hostsOnNetwork
