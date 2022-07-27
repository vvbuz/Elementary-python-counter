from ctypes import resize
from tkinter import*
import tkinter as tk

counter=0

def action_minus():
    global counter
    counter-=1
    screen.config(text=counter)

def action_plus():
    global counter
    counter+=1
    screen.config(text=counter)

def reset(*args):
    global counter
    counter=0
    screen.config(text=counter)

#GUI
interface=Tk()
interface.geometry('300x200')
interface.resizable(height=False, width=False)
interface.title('Counter')
interface.columnconfigure(1, weight=3)
screen=Label(interface, text=counter, font='Arial 50')
screen.grid(column=1, row=0, pady=30)
screen.bind("<Button-1>", reset)
b_minus=Button(interface,text='-', height=2, width=5, command=action_minus)
b_minus.grid(column=0, row=1, padx=15)
b_plus=Button(interface,text='+',height=2, width=5, command=action_plus)
b_plus.grid(column=2, row=1, padx=15)

interface.mainloop()