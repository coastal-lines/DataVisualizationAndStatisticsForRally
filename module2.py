import matplotlib.pyplot as plt
import mplcursors
from matplotlib import pylab
from pylab import *

class Obj():
    def __init__(self, x, y):
        self.x = x
        self.y = y

plt.rcParams.update({'figure.autolayout': True})
pylab.rcParams['ytick.major.pad']='8'
#prev = None
fig, ax = plt.subplots()
#fig.set_size_inches(18.5, 10.5)

b1 = Obj(1,9)
b2 = Obj(2,8)
b3 = Obj(3,6)
b4 = Obj(4,9)
b5 = Obj(5,8)
b6 = Obj(6,6)
b7 = Obj(1,9)
b8 = Obj(2,8)
b9 = Obj(3,6)
b10 = Obj(4,9)
b11 = Obj(5,8)
b12 = Obj(6,6)
b13 = Obj(1,9)
b14 = Obj(2,8)
b15 = Obj(3,6)
b16 = Obj(4,9)
b17 = Obj(5,8)
b18 = Obj(6,6)

lx = []
lx.append(b1.x)
lx.append(b2.x)
lx.append(b3.x)
lx.append(b4.x)
lx.append(b5.x)
lx.append(b6.x)
lx.append(b7.x)
lx.append(b8.x)
lx.append(b9.x)
lx.append(b10.x)
lx.append(b11.x)
lx.append(b12.x)
lx.append(b13.x)
lx.append(b14.x)
lx.append(b15.x)
lx.append(b16.x)
lx.append(b17.x)
lx.append(b18.x)
ly = []
ly.append(b1.y)
ly.append(b2.y)
ly.append(b3.y)
ly.append(b4.y)
ly.append(b5.y)
ly.append(b6.y)
ly.append(b7.y)
ly.append(b8.y)
ly.append(b9.y)
ly.append(b10.y)
ly.append(b11.y)
ly.append(b12.y)
ly.append(b13.y)
ly.append(b14.y)
ly.append(b15.y)
ly.append(b16.y)
ly.append(b17.y)
ly.append(b18.y)

labels = ["one", "two", "three", "one", "two", "three", "one", "two", "three", "one", "two", "three", "one", "two", "three", "one", "two", "three"]
ax.set(yticks = range(1, len(lx) + 1), yticklabels = labels, title="Hover over a bar")
ax.barh(lx, ly, align="center")


#work solution for detecting bar index and call method
mplcursors.cursor(ax, hover=False).connect("add", lambda sel: sel.annotation.set_text(print("bar is: " + str(sel.target.index + 1))))


plt.show()

