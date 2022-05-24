#!/bin/bash

routerIp="210.115.229.207"  # my router ip
interfaceName="usb0"

# get dynamic mobile gateway ip address from ifconfig
mobileGateway=$(ifconfig | grep -A2 $interfaceName | grep "inet " | awk -F' ' '{print $2}' | awk -F'.' '{print $1"."$2"."$3".1"}')

#sudo ip route add 210.115.229.207 via *.*.*.* dev usb0
setRoute=$(sudo ip route add $routerIp via $mobileGateway dev $interfaceName 2>&1)
