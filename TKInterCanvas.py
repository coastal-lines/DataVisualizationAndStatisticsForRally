from tkinter import *
from tkinter import ttk
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 

#WINDOW
#window - экземпляр класса tkinter
window = Tk()
window.geometry("1800x900")
window.configure(bg="black")

#TAB
#ttk.Notebook - это контейнер для таб
tabControl = ttk.Notebook(window)
tabControl.place(x = 0, y = 0, width = 1800, height = 900)
tab = ttk.Frame()
tab.place(x =0, y = 0)
tabControl.add(tab, text ='Settings')

#Frame - виджет помогающий разместить несколько областей для элементов
tabFrame = Frame(master = tab, width = 1600, height = 800, bg="blue")
tabFrame.place(x =0, y = 0)


#фрейм для авто/ручное
tabFrame2 = Frame(master = tab, width = 200, height = 200, bg="red")
tabFrame2.place(x = 1600, y = 0)

tabFrame3 = Frame(master = tab, width = 200, height = 200, bg="orange")
tabFrame3.place(x = 1600, y = 200)

tabFrame4 = Frame(master = tab, width = 1600, height = 20, bg="white")
tabFrame4.place(x = 0, y = 800)

tabFrame5 = Frame(master = tab, width = 1600, height = 20, bg="pink")
tabFrame5.place(x = 0, y = 820)


"""
#фрейм для флеш
tabFrame3 = Frame(master = tab, width = 200, height = 200, bg="red")
tabFrame3.place(x = 1500, y = 300)
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)
fig3, ax3 = plt.subplots()
ax3.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, radius=800)
ax3.axis('equal')
fig3.set_size_inches(2,2)
canvas3 = FigureCanvasTkAgg(fig3, master = tabFrame3)
canvas3.draw()
canvas3.get_tk_widget().grid()

#фрейм для секюр клиент
tabFrame4 = Frame(master = tab, width = 200, height = 200, bg="red")
tabFrame4.place(x = 1500, y = 600)
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)
fig4, ax4 = plt.subplots()
ax4.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, radius=800)
ax4.axis('equal')
fig4.set_size_inches(2,2)
canvas4 = FigureCanvasTkAgg(fig4, master = tabFrame4)
canvas4.draw()
canvas4.get_tk_widget().grid()
"""
window.mainloop() 


def test(self):
    self.tabCount = self.tabCount + 1
    tab = ttk.Frame()
    self.rootFolderName = self.commonClass.getRootFolderName()
    self.tabControl.add(tab, text = self.rootFolderName)
    self.tabControl.place(x = 0, y = 0)

