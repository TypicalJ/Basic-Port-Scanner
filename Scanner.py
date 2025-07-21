import nmap

scanner = nmap.PortScanner()

ip_addr = input('Enter IP address you want to scan: ')
print('IP you entered is: ', ip_addr)
type(ip_addr)

response = input('''\nPlease enter the type of scan you want to run
                    1)SYN ACK San
                    2) UDP Scan
                    3)Comprehensive Scan''')
print('You have selected option: ', response)

if response == '1' :
     print('Nmap Version: ', scanner.nmap_version())
     scanner.scan(ip_addr, '1-1024', '-v -sS')
     print(scanner.scaninfo())
     print("IP Status: ", scanner[ip_addr].state())
     print(scanner[ip_addr].all_protocols())
     print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif response == '2' :
     print('Nmap Version: ', scanner.nmap_version())
     scanner.scan(ip_addr, '1-1024', '-v -sU')
     print(scanner.scaninfo())
     print("IP Status: ", scanner[ip_addr].state())
     print(scanner[ip_addr].all_protocols())
     print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif response == '3' :
     print('Nmap Version: ', scanner.nmap_version())
     scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
     print(scanner.scaninfo())
     print("IP Status: ", scanner[ip_addr].state())
     print(scanner[ip_addr].all_protocols())
     print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif response >= '4' :
     print("Enter a valid option")