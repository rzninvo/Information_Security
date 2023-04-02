import os


def get_host_name_ip():
    ip_address = input("Enter your network address: ")
    groups = ip_address.split('.')
    ip_address = '.'.join(groups[:3])
    start = input("Enter the starting number: ")
    end = input("Enter the last number: ")
    return ip_address, start, end


def find_active_hosts(ip, start, end):
    file = open("result_scanIPs.txt", "a")
    file.write("\n")
    for i in range(end - start + 1):
        host = ip + "." + str(start + i)
        response = os.popen(f"ping {host}").read()
        if "Received = 4" in response:
            print(f"UP {host} Ping Successful ---> Live")
            file.write(" %s ---> Live " % host)
            file.write("\n")


def create_file():
    try:
        f = open("result_scanIPs.txt", "x")
        f.write("Ping a range of IPs and find active hosts.:\n ")
        print("New file created!")
    except:
        print("File already exists!")


ip, start, end = get_host_name_ip()
create_file()
print("Scanning in progress... ")
find_active_hosts(ip, int(start), int(end))
