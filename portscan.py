import webbrowser
import datetime
import nmap
import socket
import time

MAX_PORT = '65535'
LOCAL_IP = '127.0.0.1'



def main():

    ip = DNSrequest('www.hackthissite.org')

    clock = time.time()
    open_ports = scanOpenPorts(ip, '0-100')
    print 'time:', time.time() - clock, '\nports:', open_ports




def scanOpenPorts(ip, ports_to_scan):

    open_ports = []

    # warning
    num_ports = int(ports_to_scan.split('-')[1]) - int(ports_to_scan.split('-')[0]) + 1
    #print "warning: scanning", num_ports, "ports may take", 0.17 * num_ports, "sec."
    print "warning: scanning", num_ports, "ports may take some time"

    # scanning open ports..
    print "Start scanning the ports", ports_to_scan ,"of '" + ip + "'..."
    nmap_scan = nmap.PortScanner()
    nmap_scan.scan(ip, ports_to_scan)

    #get the open ports to list
    for port in nmap_scan[ip]['tcp']:
        if nmap_scan[ip]['tcp'][port]['state'] == 'open':
            open_ports.append(port)

    open_ports.sort()
    return open_ports


def DNSrequest(host_name):
    return socket.gethostbyname(host_name)


main()
