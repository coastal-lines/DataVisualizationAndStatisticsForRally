import matplotlib.pyplot as plt
import numpy as np

#описание оси y
plt.ylabel("Amount test cases")

#описание оси x
plt.xlabel("Folders")

#диапазон осей x и y
plt.axis([0, 20, 0, 20])

#столбцы с координатами x и y
plt.bar([2], [10])
plt.bar([2.5], [8])

#подпись к столбцам по x
plt.xticks([2.2], ["folder name"])

#показать форму
plt.show()