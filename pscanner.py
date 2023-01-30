import sys
import socket
from datetime import datetime as dt

#get target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #host to ipv4
else:
    print("Syntax: python3 pscanner.py <ip>")
    sys.exit()

#Banner
print("-"*50)
print("scanning target: " + target)
print("Time started: "+str(dt.now()))
print("-"*50)

#scan
try:
    for port in range(50,1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit()
except socket.gaierror:
    print("Error resolving host")
    sys.exit()
except socket.error:
    print("Could not conect to host")
    sys.exit()
