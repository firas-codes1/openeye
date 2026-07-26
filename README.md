# OpenEyev3
A network monitoring tool that keeps track of internet speed and devices on LAN/WLAN. 

## Methods
OpenEyev3 utilizes a method similar to that of SNMP: polling devices at fixed intervals. While SNMP is a protocol, OpenEyev3 uses ARP and ICMP protocols. 

-ARP is used to get IP addresses and MAC addresses of devices on the network using ARP Who-has broadcast. 

-ICMP is used to ping the gateway (router) and measure the rate as: Megabits / time. 


## Libraries used
-<b>netifaces</b> library is used to get the user's own IP, the gateway, and the netmask. 

-<b>Scapy</b> is used to craft ARP and ICMP packets. 

-<b>Tkinter</b> is used for the GUI.


## Future improvements
OpenEyev3 serves as a lightweight tool to monitor LAN/WLAN. However, it can be upgraded to report to a central network adminstration server, keep logs, and handle more than a single interface. In addition, security features can be added by keeping a white-list of IPs, a list of critical devices that must not disconnect, or alerting the administration in case the network speed falls below a certain limit.
