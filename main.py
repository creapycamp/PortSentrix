import socket
import termcolor

def scan(target , ports):
    print('\n'+'Starting Scan For '+ str(target))
    for port in range(1,ports):
        scan_port(target,port)


def scan_port(ipaddress,port):
    try:
        sock =socket.socket()
        sock.connect((ipaddress,port))
        print("[+] Port Open" +str(port))
        sock.close()
    except:
        pass

targets =input("Enter Targets to Scan (Split them by ',' ")
ports =int(input("Enter how many Ports You want to Scan "))
if ',' in targets:
    print(termcolor.colored("Scanning Multiple Targets",'yellow'))
    for ip_adr in targets.split(','):
        scan(ip_adr.strip(' '),ports)
else:
    scan(targets,ports)
