#!/bin/bash

#go get -u github.com/tomnomnom/assetfinder
#go install github.com/tomnomnom/assetfinder@latest
#apt install assetfinder

url=$1

if [ ! -d "$url" ];then
    mkdir $url
fi

if [ ! -d "$url/recon" ];then
    mkdir $url/recon
fi

echo "[+] Harvesting subdomains with assetfinder..."
assetfinder $url >> $url/recon/assets.txt
cat $url/recon/assets.txt | grep $1 >> $url/recon/final.txt
rm $url/recon/assets.txt
echo "[+] Done!"

