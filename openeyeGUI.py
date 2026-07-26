import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo

def CreateWindow():
	#returns: root_win, root
	root_win=tk.Tk()
	root_win.title("OpenEye v3")
	root_win.geometry('750x245+450+200')
	try:
	    root_win.iconbitmap('.\openeye.ico')
	except:
 	    print("couldnt load icon (openeye.ico) from CWD")
    
	root_win.resizable(False,False)
	style = ttk.Style(root_win)
	style.theme_use("xpnative")

	#Frames
	root=ttk.Frame(root_win,height=250,width=725)
	root.place(x=0,y=0)


	#Font sets
	fontset4=("Arial",16,"bold")
	fontset3=("Arial",16)
	#fontset2=("Arial",14,"bold")
	fontset5=("Arial",10,"bold")

	#Main text
	lbl1= tk.Label(root, text="Router: ",font = fontset3)
	lbl2= tk.Label(root, text="Internet: ",font = fontset3)

	onlbl= tk.Label(root, text="ON")
	onlbl2= tk.Label(root, text="ON")
	onlbl.configure(font = fontset4,fg="green")
	onlbl2.configure(font = fontset4,fg="green")

	timelbl=tk.Label(root,text="Speed: ",font = fontset3)
	fsl=tk.Label(root,text="Mbps",font = fontset3)

	#grid labels
	lbl1.place(x=5, y=30)
	lbl2.place(x=5, y=60)
	timelbl.place(x=5,y=2)

	fsl.place(x=220,y=2)


	return root_win,root,fontset3,fontset4,fontset5



class CreateCanvas:
        def __init__(self,root_win,root,fontset3,fontset4,fontset5):
                self.root=root
                #Canvas1 for network speed visualization
                self.canvas1 = Canvas(root,highlightthickness=1, highlightbackground="black",width=390,height=150)
                
                ##########   Second Canvas  (Devices connected)  ########
                self.canvas2= Canvas(root_win,width=0.5,height=233,bg="black")

                self.Devices=tk.Label(root, text="Devices on Network", font=fontset3)
                self.speedlbl=tk.Label(root,text="---",font = fontset4,width=7)
                #self.speedlbl2=tk.Label(root,text="1MB per",font = fontset3)
                ### Textboxes
                self.TextBox=tk.Text(root, height =13 , width = 25,font=fontset5) #for ip
                self.TextBox2=tk.Text(root, height =13 , width = 25,font=fontset5) #for mac
                
                ### Scrollbar
                self.ScrollBar=ttk.Scrollbar(root,orient='vertical',command=self.s_viewall)#(textbx.yview , textbx2.yview))
        
        def PlaceAll(self):
                self.canvas1.create_rectangle(0,150,420,0,width=0,fill="white")
                self.canvas1.place(x=5,y=90)
                self.DrawGridCanvas()
                self.canvas2.create_line(0, #x1
                    0, #y1
                    1, #x2
                    245#y2
                    , width=0.5,fill="black")
                self.canvas2.place(x=400,y=1)


                self.Devices.place(x=474,y=4) #used to be condevs

                self.TextBox.configure(yscrollcommand=self.ScrollBar.set)
                self.TextBox2.configure(yscrollcommand=self.ScrollBar.set)
                self.ScrollBar.place(x=710,y=30,height=212)

                #self.speedlbl.place(x=160,y=2)
                self.speedlbl.place(x=80,y=2)
        
        def s_viewall(self,*args):
                #for scroll bar to scroll 2 widgets at same time
                eval('self.TextBox.yview(*args)')
                eval('self.TextBox2.yview(*args)')

        def PlaceIPs(self,router,your_ip,IPlist,MAClist):
                #macs=your_mac+'\n'+router_mac+'\n' 
                self.TextBox.configure(state="normal")
                self.TextBox2.configure(state="normal")
                #trying to insert into the textbox while its state is disabled doesnt work

                self.TextBox.delete('0.0', tk.END)
                self.TextBox.insert('0.0', IPlist)

                self.TextBox2.delete('0.0', tk.END)
                self.TextBox2.insert(tk.END, MAClist)

                self.TextBox.configure(state="disable")
                self.TextBox.place(x=410,y=30)

                self.TextBox2.configure(state="disable")
                self.TextBox2.place(x=560,y=30)

        def PlaceSpeed(self,speed):
                self.speedlbl.configure(text=str(float(f'{speed:.2f}')))
                self.speedlbl.place(x=100,y=2)

        def DrawLine(self,speed,x):
                #every 1 megabit  = 15 pixel of height 
                #canvas1 has height of 150 pixels which means 10 megabits 

                y=150-(speed*15)

                if y<0 :
                        y=0 
                else:
                        pass

                self.canvas1.create_line(x, y, x,y-3 , width=4,fill="green")
                self.canvas1.place(x=5,y=90)

        def RenewCanvas(self):
                #Redraw Canvas1 when it is full (for network speed visualization)
                self.canvas1 = Canvas(self.root,highlightthickness=1, highlightbackground="black",width=390,height=150)
                self.canvas1.create_rectangle(0,150,420,0,width=0,fill="white")
                self.canvas1.place(x=5,y=90)
                self.DrawGridCanvas()

        def DrawGridCanvas(self):
                #Draw grid lines on canvas
                self.canvas1.create_line(0, 150-(15), 390,150-(15), width=0.1,fill="black")
                self.canvas1.create_line(0, 150-(15*3), 390,150-(15*3), width=0.1,fill="black")
                self.canvas1.create_line(0, 150-(15*5), 390,150-(15*5), width=0.1,fill="black")
                self.canvas1.create_line(0, 150-(15*7), 390,150-(15*7), width=0.1,fill="black")
                self.canvas1.create_line(0, 150-(15*9), 390,150-(15*9), width=0.1,fill="black")
                self.canvas1.place(x=5,y=90)


                
