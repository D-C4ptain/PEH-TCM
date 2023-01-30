#!/bin/bash
#ip sweep with bash

if [ "$1" == "" ]
then
echo "Syntax: ./ipsweep 192.168.4"
else
for ip in `seq 1 254`; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
fi

# nmap
# for ip in $(cat ips.txt); do nmap $ip; done
