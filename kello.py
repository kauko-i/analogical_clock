#!/usr/bin/env python
from Tkinter import *
import datetime
import math
def liikuta():
	global sekunti
	global minuutt
	global tunti
	try:
		taulu.delete(sekunti)
		taulu.delete(minuutti)
		taulu.delete(tunti)
	except:
		pass
	sekunti = taulu.create_line(150 + 10*math.cos(math.pi/30*int(str(datetime.datetime.now())[17:19]) - math.pi*3/2), 150 + 10*math.sin(math.pi/30*int(str(datetime.datetime.now())[17:19]) - math.pi*3/2), 150 + 100*math.cos(math.pi/30*int(str(datetime.datetime.now())[17:19]) - math.pi/2), 150 + 100*math.sin(math.pi/30*int(str(datetime.datetime.now())[17:19]) - math.pi/2), width = 1, fill="white")
	minuutti = taulu.create_line(150, 150, 150 + 80*math.cos(math.pi/30*int(str(datetime.datetime.now())[14:16]) - math.pi/2), 150 + 80*math.sin(math.pi/30*int(str(datetime.datetime.now())[14:16]) - math.pi/2), width = 2, fill="white")
	tunti = taulu.create_line(150, 150, 150 + 60*math.cos(math.pi/6*(int(str(datetime.datetime.now())[11:13]) % 12) + float(str(datetime.datetime.now())[14:16])/360*math.pi - math.pi/2), 150 + 60*math.sin(math.pi/6*(int(str(datetime.datetime.now())[11:13]) % 12) + float(str(datetime.datetime.now())[14:16])/360*math.pi - math.pi/2), width = 3, fill="white")
	root.after(1000, liikuta)

root = Tk()
root.title("Kello")

taulu = Canvas(root, height = 300, width = 300, bg = "black")
taulu.pack()
taulu.create_text(150, 30, text = "XII", font=("arial", 20), fill="white")
taulu.create_text(210, 150 - 120*math.sin(math.pi/3), text = "I", font=("arial", 20), fill="white")
taulu.create_text(150 + 120*math.sin(math.pi/3), 90, text = "II", font=("arial", 20), fill="white")
taulu.create_text(270, 150, text = "III", font=("arial", 20), fill="white")
taulu.create_text(150 + 120*math.sin(math.pi/3), 210, text = "IV", font=("arial", 20), fill="white")
taulu.create_text(210, 150 + 120*math.sin(math.pi/3), text = "V", font=("arial", 20), fill="white")
taulu.create_text(150, 270, text = "VI", font=("arial", 20), fill="white")
taulu.create_text(90, 150 + 120*math.sin(math.pi/3), text = "VII", font=("arial", 20), fill="white")
taulu.create_text(150 - 120*math.sin(math.pi/3), 210, text = "VIII", font=("arial", 20), fill="white")
taulu.create_text(30, 150, text = "IX", font=("arial", 20), fill="white")
taulu.create_text(150 - 120*math.sin(math.pi/3), 90, text = "X", font=("arial", 20), fill="white")
taulu.create_text(90, 150 - 120*math.sin(math.pi/3), text = "XI", font=("arial", 20), fill="white")
liikuta()

root.mainloop()
