import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
import mplcursors
import pandas as pd
from tkinter import *

dpi = 96
plt.rcParams['figure.figsize']=(1200 / dpi, 800 / dpi)
plt.rcParams.update({'figure.autolayout': True})
#sns.set_style('darkgrid')

fig, ax = plt.subplots()

x = ['zero', 'one', 'two', 'three', 'four', 'five']
y = [0.5,1,2,3,4,5]
y2 = [6,7,8,9,10,11]

df = pd.DataFrame({
    'Factor': x,
    'W': y,
    'W2': y2
})

print(df)

tidy = df.melt(id_vars='Factor').rename(columns=str.title)
print(tidy)

ax = sns.barplot(y='Factor', x='Value', hue='Variable', data=tidy)

ax.set_xlim(0, max(y2) + 1)
ax.set_xticks(range(1, max(y2) + 1))



#plt.show()

window = Tk() 
window.title('Plotting in Tkinter')
window.geometry("1100x800")

canvas = Canvas(master = window, width = 1100, height = 800)
canvas.place(x = 0, y = 0)
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().grid(row=0,column=1)

toolbar = NavigationToolbar2Tk(canvas, window, pack_toolbar=False)
toolbar.update()
def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)

mplcursors.cursor(ax, hover=False).connect("add", lambda sel: sel.annotation.set_text(print("bar is: " + str(sel.target.index + 1))))

window.mainloop() 