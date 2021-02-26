# library
import matplotlib.pyplot as plt

plt.figure(figsize=(40,4))
# Make fake dataset
height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
 
# Choose the position of each barplots on the x-axis (space=1,4,3,1)
y_pos = [0,0.5,1,1.5,2]
 
# Create bars
plt.barh(y_pos, width=height,height=0.1)
 
# Create names on the x-axis
plt.yticks(y_pos, bars)
 
# Show graphic
plt.show()