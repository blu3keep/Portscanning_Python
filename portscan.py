import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(0.05)

address = input('Enter the address to scan: ')

print('1 - To specific port on '+address)
print('2 - for all ports in '+address)

option = input('Choose an option: ')

if option == '1':
    port = input('Enter with the port: ')
    code = client.connect_ex((address, int(port)))
    if code == 0:
        print('Open port!')
    client.close()
else:
    option == '2'
    file = open('Open-ports.txt', 'w')
    for port in range(1, 65535):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.05)
        code = client.connect_ex((address, int(port)))
        if code == 0:
            print('Open port: '+str(port))
            file.write(f'Open port: {str(port)}\n')
        client.close()