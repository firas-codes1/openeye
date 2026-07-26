from scapy.all import *
import threading
import time

def ScanOthers(routerip,yourip,netmask):
    ReservedCounter=0
    for block in netmask:
        if block=="0":
            break
        elif block==".":
            ReservedCounter+=1

    LANrange=""
    for number in routerip:
        if number==".":
            ReservedCounter-=1
            LANrange=LANrange+number
            if ReservedCounter==0:
                break #got the range

        else:
            LANrange=LANrange+number

    IPlist=[yourip,routerip]
    MAClist=["(You)","(Router)"]

    t_1=threading.Thread(target=ScanThread,args=(0,50,IPlist,MAClist,yourip,routerip,LANrange))
    t_2=threading.Thread(target=ScanThread,args=(51,100,IPlist,MAClist,yourip,routerip,LANrange))
    t_3=threading.Thread(target=ScanThread,args=(101,150,IPlist,MAClist,yourip,routerip,LANrange))
    t_4=threading.Thread(target=ScanThread,args=(151,200,IPlist,MAClist,yourip,routerip,LANrange))
    t_5=threading.Thread(target=ScanThread,args=(201,255,IPlist,MAClist,yourip,routerip,LANrange))
    print("Started threads for scanning...")
    t_1.start()
    t_2.start()
    t_3.start()
    t_4.start()
    t_5.start()

    t_1.join()
    t_2.join()
    t_3.join()
    t_4.join()
    t_5.join()
    print("Scanning completed.")
    return  IPlist,MAClist    

def ScanThread(counter,counterLimit,IPlist,MAClist,yourip,routerip,LANrange):
    while counter<=counterLimit:
        target_ip=LANrange+str(counter)
        if target_ip==yourip or target_ip==routerip:
            pass
        else:
            arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst=target_ip)
            try:
                arp_response = srp(arp_request, timeout=1, verbose=False)[0]
            except:
                print("Something is wrong, couldnt send ARP Who-has "+target_ip+" packet")
                    
            for sent, received in arp_response:

                target_mac = received.hwsrc
                MAClist.append(target_mac)
                IPlist.append(target_ip)
                #placecds()

        counter+=1
        #print(IPlist,MAClist)



def GetRouterAvg(routerip):
    times=0
    sizes=0

    for i in range(0,4):
        t1,size1,size2=PingRouterThread(routerip)
        times+=t1
        sizes+=size1+size2

    AvgRate=(sizes*0.000008)/times #convert bytes to megabits 

    return AvgRate 
    #3 units: bytes sent, time, and convert them to megabits 
    #convert bytes to megabits 
    #divide by time normally 

def PingRouterThread(routerip):
    
    pack=IP(dst=routerip)/ICMP()
    size1=len(bytes(pack))
    
    start=time.time()
    
    ans ,unans = sr(pack, verbose=0)
    
    stop=time.time()
    t=stop-start

    if len(ans)>0:
        sent, received = ans[0]
        size2=len(bytes(received))
    else:
        print("Failed to ping router")

    return t, size1, size2 
    


def WriteScan(yourip,routerip,IPlist,MAClist,CanvasObj):
    ips=""
    macs=""
    for ip in IPlist:
        ips=ips+ip+'\n'

    for mac in MAClist:
        macs=macs+mac+'\n'

    CanvasObj.PlaceIPs(yourip,routerip,ips,macs)
