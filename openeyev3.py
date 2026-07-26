import netifaces
import openeyeGUI
import openeyeThreads
import sys
import threading


MyGateway=netifaces.gateways()["default"][2][0] #get IP of gateway

iface_name = str(netifaces.gateways()["default"][2][1]) #interface name

YourIP=(netifaces.ifaddresses(iface_name)[2][0]["addr"]) #your ip

Netmask=netifaces.ifaddresses(iface_name)[2][0]["netmask"] #netmask

root_win,root,fontset3,fontset4,fontset5=openeyeGUI.CreateWindow()
Canvas=openeyeGUI.CreateCanvas(root_win,root,fontset3,fontset4,fontset5)
Canvas.PlaceAll()

Scan=threading.Thread(target=openeyeThreads.ScanWriteThread,args=(MyGateway,YourIP,Netmask,Canvas))
Scan.start()

Speed=threading.Thread(target=openeyeThreads.RouterPingThread,args=(MyGateway,Canvas))
Speed.start()


root_win.mainloop()
exitflag=1
sys.exit()
