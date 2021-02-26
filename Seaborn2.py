import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
import mplcursors
import pandas as pd

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

mplcursors.cursor(ax, hover=False).connect("add", lambda sel: sel.annotation.set_text(print("bar is: " + str(sel.target.index + 1))))

plt.show()

