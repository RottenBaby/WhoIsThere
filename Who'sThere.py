from scapy import *
import argparse

from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp1

print("""
     Who's There?
            ,--.!,  
         __/   -*-
       ,d08b.  '|`
       0088MM     
       `9MMP'     
   by  RottenBaby
     Version 1.0
""")


def Argumetn():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--from", dest="fromPort", help="from port")
    parser.add_argument("-t", "--to", dest="toPort", help="to port")
    return parser.parse_args()

args = Argumetn()
FromPort = int(args.fromPort)
ToPort = int(args.toPort)





def WhoIsTher(FromPort,ToPort):
    print("[*] Scan From "+ str(FromPort) +" to " + str(ToPort))
    for port in range(FromPort, ToPort):

        ip = "192.168.1."+ str(port)
        pack = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip, hwdst="ff:ff:ff:ff:ff:ff")
        packresp = srp1(pack, timeout=1, verbose=0,)
        if packresp:
            print("[+]IP: " + packresp.psrc + " MAC: "+ packresp.hwsrc)
        else:
            pass
            #print("[OFF line]"+ip)


WhoIsTher(FromPort, ToPort)
