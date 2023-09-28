#!/usr/bin/python3
import socket
import threading
import time

banner = '''
********************************************
*    SimplePortScanner                     *
*    by cloud                              *
********************************************
'''
print(banner)
host = input("Enter Your target IP: ")

port1 = int(input("Enter the staring port: "))
port2 = int(input("Enter the ending port: "))

print(f"Scanning started on {host} from port {port1} to {port2}")

start_time = time.time()
def scan_port(ports):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)

            result = s.connect_ex((host,ports))
            if result ==0:
                print(f'Port {ports} is Open')
            s.close() 
        except:
             pass  
          


for ports in range(port1, port2 +1):
    
    thread = threading.Thread(target=scan_port, args=(ports,))
    thread.start()

end_time = time.time()

print("------------------------")
print(f"Time taken: {round(end_time-start_time,2)} seconds")
print("------------------------")
