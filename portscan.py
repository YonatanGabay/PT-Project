from scapy.all import *
import webbrowser, nmap, random, threading


MAX_PORT = '65535'
LOCAL_IP = '127.0.0.1'



def main():

    ip = DNSrequest('www.google.com')

    clock = time.time()
    open_ports = scanOpenPorts(ip, '0-100')#+MAX_PORT)
    print 'time:', time.time() - clock, '\nports:', open_ports



def scanOpenPorts(dest_ip, ports_to_scan):

    open_ports = []

    # warning
    num_ports = int(ports_to_scan.split('-')[1]) - int(ports_to_scan.split('-')[0]) + 1
    print "warning: scanning", num_ports, "ports may take", 0.17 * num_ports, "sec."

    # scanning open ports..
    print "Start scanning the ports", ports_to_scan ,"of '" + dest_ip + "'..."
    nmap_scan = nmap.PortScanner()
    nmap_scan.scan(dest_ip, ports_to_scan)

    #get the open ports to list
    for port in nmap_scan[dest_ip]['tcp']:
        if nmap_scan[dest_ip]['tcp'][port]['state'] == 'open':
            open_ports.append(port)

    open_ports.sort()
    return open_ports


def DNSrequest(host_name):
    return socket.gethostbyname(host_name)


main()
