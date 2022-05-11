#!/bin/bash

homeRouterIp="210.115.229.207"
interfaceName="usb0"
mobileGateway=$(ifconfig | grep -A2 $interfaceName | grep "inet " | awk -F' ' '{print $2}' | awk -F'.' '{print $1"."$2"."$3".1"}')

setRoute=$(sudo ip route add $homeRouterIp via $mobileGateway dev $interfaceName 2>&1)

#sudo ip route add 1.2.3.4 via *.*.*.* dev usb0