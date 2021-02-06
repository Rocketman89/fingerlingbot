#!/bin/bash

netconnect=$(ping -c 1 8.8.8.8 | grep packet | awk '{print $6}' | awk -F% '{print $1}') 

if [[ $netconnect == "0" ]]
then
	sudo apt-get install lame
else
	tar -xvf lame.tar.gz .
fi
sudo cp ./lame /usr/bin/


