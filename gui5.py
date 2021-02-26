from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
import seaborn as sns
import mplcursors
import pandas as pd

tabCount = 0

def createMainTab():
    tab = ttk.Frame()

    tabControl.add(tab, text ='Settings')
    tabControl.place(x = 0, y = 0, width = 400, height = 200)

    lbl1 = Label(master = tab, text="Server:")
    lbl1.place(x = 0, y = 0, width=100)
    txt1 = Entry(master = tab)
    txt1.place(x = 100, y = 0, width=200)
    lbl2 = Label(master = tab, text="User:")
    lbl2.place(x = 0, y = 20, width=100)
    txt2 = Entry(master = tab)
    txt2.place(x = 100, y = 20, width=200)
    lbl3 = Label(master = tab, text="Password:")
    lbl3.place(x = 0, y = 40, width=100)
    txt3 = Entry(master = tab)
    txt3.place(x = 100, y = 40, width=200)

    lbl4 = Label(master = tab, text="Workspace:")
    lbl4.place(x = 0, y = 60, width=100)
    txt4 = Entry(master = tab)
    txt4.place(x = 100, y = 60, width=200)
    lbl5 = Label(master = tab, text="Project:")
    lbl5.place(x = 0, y = 80, width=100)
    txt5 = Entry(master = tab)
    txt5.place(x = 100, y = 80, width=200)
    lbl6 = Label(master = tab, text="Root folder:")
    lbl6.place(x = 0, y = 100, width=100)
    txt6 = Entry(master = tab)
    txt6.place(x = 100, y = 100, width=200)

    btn = Button(master = tab, text = "Start session")
    btn.place(x = 100, y = 120, width=200)

def plot2():
    global tabCount
    tabCount = tabCount + 1

    #matplotlib frame 
    tab = ttk.Frame()
    tabControl.add(tab, text ='Tab ' + str(tabCount))
    tabControl.place(x = 0, y = 0)
    #frameCanvas = Frame(master = window, width = 1100, height = 800, bg="white")
    #frameCanvas.place(x = 0, y = 50)
    canvas = Canvas(master = tab, width = 1100, height = 800)
    canvas.place(x = 0, y = 0)

    dpi = 96
    plt.rcParams['figure.figsize']=(1050 / dpi, 750 / dpi)
    plt.rcParams.update({'figure.autolayout': True})

    fig, ax = plt.subplots()

    fig.suptitle('Main title')

    x = ['zero', 'one', 'two', 'three', 'four', 'five']
    y = [0.5,1,2,3,4,5]
    y2 = [6,7,8,9,10,11]

    df = pd.DataFrame({
        'Factor': x,
        'manual': y,
        'automated': y2
    })

    print(df)

    tidy = df.melt(id_vars='Factor').rename(columns=str.title)
    print(tidy)

    ax = sns.barplot(y='Factor', x='Value', hue='Variable', data=tidy)

    ax.set_xlim(0, max(y2) + 1)
    ax.set_xticks(range(1, max(y2) + 1))

    mplcursors.cursor(ax, hover=False).connect("add", lambda sel: sel.annotation.set_text(print("bar is: " + str(sel.target.index + 1))))

    canvas = FigureCanvasTkAgg(fig, master=tab)
    canvas.draw()
    canvas.get_tk_widget().grid()

#actions
def getText():
    print(txt.get())

#tkinter
window = Tk()
#title
window.title("Rally Data Visualization and Prediction")
window.geometry("1400x900")



#tabs holder
tabControl = ttk.Notebook(window)
createMainTab()

#elements frame
frameElements = Frame(master = window, width = 1100, height = 20)
frameElements.place(x = 0, y = 830)

lbl = Label(master = frameElements, text="Query input:")
lbl.place(x = 0, y = 0, width=100)
txt = Entry(master = frameElements)
txt.place(x = 100, y = 0, width=900)
btn = Button(master = frameElements, text = "Find test cases", command = plot2)
btn.place(x = 1000, y = 0, width=92)

#endles loop for wait any user interactions - will works during window is opened
window.mainloop()