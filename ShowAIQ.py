import tkinter as tk 
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np


#Func calling next window with details
def GetDetails(cityValue):
    #newwin = tk.Toplevel(master)
    #newwin.geometry("250x250+700+500")
    #l1 = Label(newwin, text=city)
    #l1.pack()

    fig = plt.figure()
    #ax = fig.add_axes([0,0,1,1])
    ax = plt.axes()
    days = ['Jan', 'Feb', 'Mar', 'April', 'May','June','July','August','Sept','Oct','Nov','Dec']
    #values = [23,17,35,29,12,25,19,26,75,22,11,25]
    plt.plot(days, cityValue)
    ax.set_xlabel('Months')
    ax.set_ylabel('AQI Level')
    #plt.xlabel('Months')
    #plt.ylabel('AQI Level')
    plt.show()

# creating main tkinter window/toplevel 
master = tk.Tk()
master.geometry("180x460+800+300")


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        master.destroy()

# this wil create a label widget 
l1 = Label(master, text = "Delhi") 
l2 = Label(master, text = "AhmedaBad")
l3 = Label(master, text = "Bengaluru")
l4 = Label(master, text = "Pune")
l5 = Label(master, text = "Chennai")
l6 = Label(master, text = "Hyderabad")
l7 = Label(master, text = "Lucknow")
l8 = Label(master, text = "Kolkata")
l9 = Label(master, text = "Bhopal")
l10 = Label(master, text = "Amritsar")
l11 = Label(master, text = "Jaipur")
l12 = Label(master, text = "Agra")
l13 = Label(master, text = "Patna")
l14 = Label(master, text = "Mumbai")
l15 = Label(master, text = "Trivandrum")

# rows and columns as specified 
l1.grid(row = 0, column = 0, sticky = W, pady = 2) 
l2.grid(row = 1, column = 0, sticky = W, pady = 2)
l3.grid(row = 2, column = 0, sticky = W, pady = 2)
l4.grid(row = 3, column = 0, sticky = W, pady = 2)
l5.grid(row = 4, column = 0, sticky = W, pady = 2)
l6.grid(row = 5, column = 0, sticky = W, pady = 2)
l7.grid(row = 6, column = 0, sticky = W, pady = 2)
l8.grid(row = 7, column = 0, sticky = W, pady = 2)
l9.grid(row = 8, column = 0, sticky = W, pady = 2)
l10.grid(row = 9, column = 0, sticky = W, pady = 2)
l11.grid(row = 10, column = 0, sticky = W, pady = 2)
l12.grid(row = 11, column = 0, sticky = W, pady = 2)
l13.grid(row = 12, column = 0, sticky = W, pady = 2)
l14.grid(row = 13, column = 0, sticky = W, pady = 2)
l15.grid(row = 14, column = 0, sticky = W, pady = 2)
DelhiValue = [257,284,220,174,174,189,179,174,174,260,370,165]
AhmedaBadValue = [257,284,220,174,174,189,179,174,174,260,370,165]
BengaluruValue = []
PuneValue = []
ChennaiValue = []
HyderbadValue = []
LucknowValue = []
KolkataValue = []
BhopalValue = []
AmritsarValue = []
JaipurValue = []
AgraValue = []
PatnaValue = []
MumbaiValue = []
TrivandrumValue = []


#Button for click
b1 = Button(master, text = "Polution Level", background="#00a9e0" , command = lambda: GetDetails(DelhiValue))
b2 = Button(master, text = "Polution Level", background="#00a9e0", command = lambda: GetDetails(AhmedaBadValue))
b3 = Button(master, text = "Polution Level", background="#00a9e0", command = lambda: GetDetails(BengaluruValue))
b4 = Button(master, text = "Polution Level", background="#00a9e0", command = lambda: GetDetails(PuneValue))
b5 = Button(master, text = "Polution Level", background="#00a9e0", command = lambda: GetDetails(ChennaiValue))
b6 = Button(master, text = "Polution Level", background="#00a9e0", command = lambda: GetDetails(HyderbadValue))
b7 = Button(master, text = "Polution Level", background="#00a9e0", command = lambda: GetDetails(LucknowValue))
b8 = Button(master, text = "Polution Level", background="#00a9e0", command = lambda: GetDetails(KolkataValue))
b9 = Button(master, text = "Polution Level", background="#00a9e0", command = lambda: GetDetails(BhopalValue))
b10 = Button(master, text = "Polution Level", background="#00a9e0", command = lambda: GetDetails(AmritsarValue))
b11 = Button(master, text = "Polution Level", background="#00a9e0", command = lambda: GetDetails(JaipurValue))
b12 = Button(master, text = "Polution Level", background="#00a9e0", command = lambda: GetDetails(AgraValue))
b13 = Button(master, text = "Polution Level", background="#00a9e0", command = lambda: GetDetails(PatnaValue))
b14 = Button(master, text = "Polution Level", background="#00a9e0", command = lambda: GetDetails(MumbaiValue))
b15 = Button(master, text = "Polution Level", background="#00a9e0", command = lambda: GetDetails(TrivandrumValue))
#arranging buttons
b1.grid(row = 0, column = 1, sticky = W, pady = 2)
b2.grid(row = 1, column = 1, sticky = W, pady = 2)
b3.grid(row = 2, column = 1, sticky = W, pady = 2)
b4.grid(row = 3, column = 1, sticky = W, pady = 2)
b5.grid(row = 4, column = 1, sticky = W, pady = 2)
b6.grid(row = 5, column = 1, sticky = W, pady = 2)
b7.grid(row = 6, column = 1, sticky = W, pady = 2)
b8.grid(row = 7, column = 1, sticky = W, pady = 2)
b9.grid(row = 8, column = 1, sticky = W, pady = 2)
b10.grid(row = 9, column = 1, sticky = W, pady = 2)
b11.grid(row = 10, column = 1, sticky = W, pady = 2)
b12.grid(row = 11, column = 1, sticky = W, pady = 2)
b13.grid(row = 12, column = 1, sticky = W, pady = 2)
b14.grid(row = 13, column = 1, sticky = W, pady = 2)
b15.grid(row = 14, column = 1, sticky = W, pady = 2)
master.protocol("WM_DELETE_WINDOW", on_closing)
master.mainloop()