import openeyeNet
import time 

def ScanWriteThread(routerip,yourip,netmask,CanvasObj):
	while 1:
		IPlist,MAClist =openeyeNet.ScanOthers(routerip,yourip,netmask)
		openeyeNet.WriteScan(yourip,routerip,IPlist,MAClist,CanvasObj)
		time.sleep(15)

def RouterPingThread(routerip,CanvasObj):
	x=0
	while 1:
		if x>=380:
			x=0
			#renew canvas! 
			CanvasObj.RenewCanvas()
		else:
			pass

		speed=openeyeNet.GetRouterAvg(routerip)
		CanvasObj.PlaceSpeed(speed)
		CanvasObj.DrawLine(speed,x)
		time.sleep(1)
		x+=4 #space between each line 