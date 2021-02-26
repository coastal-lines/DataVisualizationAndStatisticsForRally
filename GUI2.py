from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 

#plot
def plot(): 
    fig = Figure(figsize=(5, 4), dpi=100)
    index = ["0","1","2","3","4"]
    values = [5,7,3,4,6]
    plt.bar(index,values)
    ax = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master = frameCanvas)
    canvas.draw()
    canvas.get_tk_widget().grid()
    frame = Frame(master = frameCanvas, width = 1200, height = 800)
    #frame.grid(row=0, column=1)
    toobar = NavigationToolbar2Tk(canvas, frame)
    #canvas.get_tk_widget().grid(row=1, column=0)

#actions
def getText():
    print(txt.get())

#tkinter
window = Tk()
#title
window.title("Rally Data Visualization and Prediction")
window.geometry("1400x900")


frameCanvas = Frame(window, width = 1200, height = 800, bg="white")
frameCanvas.grid(column = 0, row = 0)
canvas = Canvas(master = frameCanvas, width = 1200, height = 800, bg="black")
canvas.place(x = 0, y = 0)

"""
fig = Figure(figsize=(5, 4), dpi=100)
index = ["0","1","2","3","4"]
values = [5,7,3,4,6]
plt.bar(index,values)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master = frameCanvas)
canvas.draw()
canvas.get_tk_widget().grid(row=2, column=0)
frame = Frame(master = frameCanvas, width = 1200, height = 800)
toobar = NavigationToolbar2Tk(canvas, frame)
"""


frameElements = Frame(window, width = 1200, height = 20, bg="yellow")
frameElements.grid(column = 0, row = 1, sticky="ew")
lbl = Label(master = frameElements, text="Query input:")
lbl.grid(sticky="W",column = 0, row = 1)
txt = Entry(master = frameElements, width = 100)
txt.grid(sticky="W",column = 1, row = 1)
btn = Button(master = frameElements, text = "Find test cases", command = plot)
btn.grid(sticky="W",column = 2, row = 1)

#endles loop for wait any user interactions - will works during window is opened
window.mainloop()

#sticky="W", 