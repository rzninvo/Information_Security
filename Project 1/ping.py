import os
import socket
import re


def get_host_name_ip():
    get_input = input("Enter your ip address/domain: ")
    try:
        if re.search("[a-zA-Z]", get_input):
            ip_address = socket.gethostbyname(get_input)
            domain_name = get_input
        else:
            ip_address = get_input
            domain_name = ""
    except:
        print("Unable to get Hostname and IP")
    return domain_name, ip_address


def create_file():
    try:
        f = open("result_ping.txt", "x")
        f.write("Ping a range of IPs and find active hosts:\n ")
        print("New file created!")
    except:
        print("File already exists!")


domain, ip = get_host_name_ip()
create_file()
print("Pinging " + domain + " : " + ip)
response = os.system("ping " + ip)
file = open("result_ping.txt", "a")
file.write("\n")
file.write(os.popen(f"ping {ip}").read())
file.write("\n")
file.write("-----------------------------------------------------")
