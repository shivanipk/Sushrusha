'''
Created on 24-Oct-2016

@author: Administrator
'''

import tkinter
from tkinter import Menu
#from ScrolledText import *
#from scrolledtext import * ;
import tkinter.scrolledtext as tkst
mf=tkinter.Tk()

mf.geometry("1000x1000+10+10")
mf.title("AI ASSISTANT")
malabel=tkinter.Label(mf,text="my label").pack()

textPad = tkst.ScrolledText(mf, width=100, height=80)
textPad.pack()
menubar=Menu(mf)
 
patientmenu=Menu(menubar)
patientmenu.add_command(label="new")
patientmenu.add_command(label="open")
patientmenu.add_command(label="save")
patientmenu.add_command(label="preview")
menubar.add_cascade(label="file",menu=patientmenu)

helpmenu=Menu(menubar)
helpmenu.add_command(label="help")
helpmenu.add_command(label="about")
helpmenu.add_command(label="help")
menubar.add_cascade(label="help",menu=helpmenu)

exitmenu=Menu(menubar)
exitmenu.add_command(label="Exit")
menubar.add_cascade(label="exit",menu=exitmenu)
'''menubar.add_cascade(cnf)'''
mf.config(menu=menubar)

mf.mainloop()
 










 

