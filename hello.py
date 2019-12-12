import tkinter as tk 
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

# creating main tkinter window/toplevel 
master = tk.Tk()
master.geometry("180x180+700+300")

#Func calling next window with details
def GetDetails(city):
    #newwin = tk.Toplevel(master)
    #newwin.geometry("250x250+700+500")
    #l1 = Label(newwin, text=city)
    #l1.pack()
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    days = ['Mon', 'Tue', 'Wed', 'Thurs', 'Fri','Sat','Sun']
    values = [23,17,35,29,12,25,19]
    ax.bar(days,values)
    ax.set_xlabel('Day')
    ax.set_ylabel('AQI Level')
    plt.show()


# this wil create a label widget 
l1 = Label(master, text = "Delhi") 
l2 = Label(master, text = "Mumbai")
l3 = Label(master, text = "Kolkata")
l4 = Label(master, text = "Chennai")
l5 = Label(master, text = "Bengaluru")


# rows and columns as specified 
l1.grid(row = 0, column = 0, sticky = W, pady = 2) 
l2.grid(row = 1, column = 0, sticky = W, pady = 2)
l3.grid(row = 2, column = 0, sticky = W, pady = 2)
l4.grid(row = 3, column = 0, sticky = W, pady = 2)
l5.grid(row = 4, column = 0, sticky = W, pady = 2)

#Button for click
b1 = Button(master, text = "Polution Level", background="#00a9e0" , command = lambda: GetDetails("Delhi"))
b2 = Button(master, text = "Polution Level", background="#00a9e0")
b3 = Button(master, text = "Polution Level", background="#00a9e0")
b4 = Button(master, text = "Polution Level", background="#00a9e0")
b5 = Button(master, text = "Polution Level", background="#00a9e0")
#arranging buttons
b1.grid(row = 0, column = 1, sticky = W, pady = 2)
b2.grid(row = 1, column = 1, sticky = W, pady = 2)
b3.grid(row = 2, column = 1, sticky = W, pady = 2)
b4.grid(row = 3, column = 1, sticky = W, pady = 2)
b5.grid(row = 4, column = 1, sticky = W, pady = 2)

mainloop()