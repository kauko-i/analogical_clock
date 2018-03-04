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

roomalaiset_numerot = ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII")
taulu = Canvas(root, height = 300, width = 300, bg = "black")
taulu.pack()
for i in range(12):
	taulu.create_text(150 + 120*math.cos(i*math.pi/6-math.pi/3), 150 + 120*math.sin(i*math.pi/6-math.pi/3), text = roomalaiset_numerot[i], font = ("arial", 20), fill = "white")
liikuta()

root.mainloop()
