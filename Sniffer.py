#!/usr/bin/env python
from scapy.all import *
from datetime import datetime
import urllib.request
import urllib.parse
import csv

# Holds addresses
clientprobes = []
location = 'home'
count = 0


def PacketHandler(pkt):
    # filter if packet is probe request
    if pkt.haslayer(Dot11ProbeReq):
       # only packes with an ssid are shown.
       # Is packet is a wildcard in wireshark it will not be shown
        if len(pkt.info) > 0:
            # shows packet mac address
            testcase = (pkt.addr2, '---', pkt.info)
        else:
            pkt.info = "Unknown"
            testcase = (pkt.addr2, pkt.info)
        if testcase not in clientprobes:
            # decode pkt.info so b ' is not in the beginning
            pkt_info = pkt.info.decode("utf-8").replace(' ', '_')

            # datetime object containing current date and time
            now = datetime.now()
            time_log = now.strftime('%m/%d/%y_%H:%M:%S')
            clientprobes.append(testcase)
            print("New Probe Found: ", pkt.addr2,
                  ' ',  ' ', pkt_info, ' ', time_log)
            SendtoServer(str(pkt.addr2), str(pkt_info),
                         str(location), str(time_log))
            with open('data.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow(['MAC', 'SSID', 'Time'])
                writer.writerow([pkt.addr2, pkt_info, time_log])


def SendtoServer(MAC, SSID, Location, Time):
    url = ('YOUR_HOSTED_LOCATION/add_data.php?MAC=' + MAC +
           '&SSID='+SSID+'&Location='+Location+'&TIME='+Time + '/')
    # +'/',':/')
    print(url)
    # Can be used to replace characters that dont get parsed correctly
    # Might not need to do this though. It still might go through with
    # %3 and %20 because the system knows those represent white space and ':'
    #url = url.replace('%3',':')
    wp = urllib.request.urlopen(url)
    pw = wp.read()
    print(pw)


sniff(iface='wlan0mon', prn=PacketHandler, store=0)
print('after sniff')
