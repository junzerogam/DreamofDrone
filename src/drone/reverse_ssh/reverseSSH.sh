#!/bin/bash

mobileInterfaceName="usb0"
routerIp="210.115.229.207" # my router ip

mobileIpAddress=$(ifconfig | grep -A2 $mobileInterfaceName | grep "inet " | awk -F' ' '{print $2}')

ssh $mobileIpAddress -f -N -T -R 2222:localhost:22 uhyeong@$routerIp -p 5001
