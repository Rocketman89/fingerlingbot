#!/bin/bash

netconnect=$(ping -c 1 8.8.8.8 -I eth0 | grep packet | awk '{print $6}' | awk -F% '{print $1}') 

if [[ $netconnect == "0" ]]
then
	sudo git clone https://github.com/markondej/fm_transmitter
else
	tar -xvf fm_transmitter_markondej.tar.gz .
fi

sudo apt-get install gcc g++ make
cd fm_transmitter
sudo make

#USAGE:
#GPIO pin 4 needs a wire
#sudo ./fm_transmitter [-f frequency] [-r] filename
#sudo ./fm_transmitter -f 100 -r star_wars.wav
