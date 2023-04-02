import socket

def create_plain_server(port = 3000):
    s = socket.socket()
    print("Socket successfully created")
    s.bind(('', port))
    print("Socket binded to %s" % port)
    s.listen(5)
    print("Socket is listening")
    while True:
        c, addr = s.accept()
        print('Got connection from', addr)
        c.send('Hello there!'.encode())
        c.close()
        break

def create_mid_server(port= 3000):
    s = socket.socket()
    print("Socket successfully created")
    s.bind(('', port))
    print("Socket binded to %s" % port)
    s.listen(5)
    print("Socket is listening")
    while True:
        c, addr = s.accept()
        print('Got connection from', addr)
        data = c.recvfrom(6000)
        print(f'Recieved client system info: {data}')
        c.send('Data recieved. Thanks chump!'.encode())
        c.close()
        break

def create_full_server(port= 3000):
    s = socket.socket()
    print("Socket successfully created")
    s.bind(('', port))
    print("Socket binded to %s" % port)
    s.listen(5)
    print("Socket is listening")
    while True:
        c, addr = s.accept()
        print('Got connection from', addr)
        while True:
            option = (input('What are you going to do?\t 1.sysinfo\t 2.close the connection\n')).lower()
            c.send(option.encode())
            if option == 'sysinfo' or option == '1':
                data = c.recvfrom(6000)
                print(f'Recieved client system info: {data}')
                c.send('Data recieved. Thanks chump!'.encode())
            elif option == 'close' or option == '2':
                c.send('close'.encode())
                c.close()
                print('Closing the connection...')
                break
        break

create_full_server()