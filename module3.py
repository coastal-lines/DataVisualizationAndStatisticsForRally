import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import mplcursors

#описание оси y
plt.ylabel("Amount test cases")

#описание оси x
plt.xlabel("Folders")

#диапазон осей x и y
plt.axis([0, 20, 0, 20])

#столбцы с координатами x и y
b1 = plt.bar([2], [10])
b1.set_label("999")
plt.bar([2.5], [8])
plt.bar([4], [1], picker=True)
plt.bar([4.5], [3], picker=True)

#подпись к столбцам по x
#plt.xticks([2.2], ["folder name"])
plt.xticks(range(9))

cursor = mplcursors.cursor() # or just mplcursors.cursor()

@cursor.connect("add")
def on_add(sel):
    #bar_num = sel.target.index + 1
    #print(bar_num)
    global prev
    bar_num = sel.target.index + 1
    postfix = "st"
    print(f"You hovered over the {bar_num}{postfix} bar.")
    prev = bar_num

#показать форму
plt.show()