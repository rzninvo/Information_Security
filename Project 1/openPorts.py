from socket import *


def get_host_name_ip():
    ip_address = input("Enter your host IP address: ")
    start = input("Enter the start port number: ")
    end = input("Enter the last port number: ")
    return ip_address, start, end


def find_open_ports(ip, start, end):
    print("IP --> " + ip)
    file = open("result_openPorts.txt", "a")
    file.write("\n")
    file.write("IP %s :" % ip)
    for port in range(start, end):
        s = socket()
        conn = s.connect_ex((ip, port))
        if conn == 0:
            print("Port %d: OPEN" % (port,))
            file.write("\n")
            file.write("Port %d: OPEN" % (port,))
        s.close()


def create_file():
    try:
        f = open("result_openPorts.txt", "x")
        f.write("Scan an IP and find open ports:\n ")
        print("New file created!")
    except:
        print("File already exists!")


ip, start, end = get_host_name_ip()
create_file()
print("Scanning in progress... ")
find_open_ports(ip, int(start), int(end))
