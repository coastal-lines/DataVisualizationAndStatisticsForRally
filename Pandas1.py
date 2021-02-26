import pandas as pd
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
import seaborn as sns
import mplcursors
import pandas as pd
from pyral import Rally, rallyWorkset

ids = ['TF15976', 'TF16518', 'TF18747', 'TF19778', 'TF20258', 'TF20310', 'TF20687', 'TF21795']
names = ['1', '2', '3', '4', '5', '6', '7', '8']
manual = [6, 0, 3, 0, 9, 1, 0, 1]
automated = [2, 2, 30, 17, 10, 7, 8, 6]

df = pd.DataFrame({
    'ids': ids,
    'names': names,
    'manual': manual,
    'automated': automated
})

#tidy = pd.melt(df, id_vars=['names'], value_vars=['manual', 'automated'], var_name='999', value_name='names')
tidy = df.melt(id_vars='names', value_vars=['manual', 'automated'])

print(df)
print("---")
print(tidy)

window = Tk()

#title
window.title("Rally Data Visualization and Prediction")
window.geometry("1650x900")

fig, ax = plt.subplots()

#get root folder name
fig.suptitle("99999999999")

ax = sns.barplot(y='names', x='value', hue='variable', data = tidy)

plt.show()