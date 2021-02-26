from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 

# plot function is created for  
# plotting the graph in  
# tkinter window 
def plot(): 

    #Figure - это контейнер самого верхнего уровня, та область на которой все нарисовано. Таких областей может быть несколько, каждая из которых может содержать несколько контейнеров Axes.
    fig = plt.figure()
    index = ["0","1","2","3","4"]
    values = [5,7,3,4,6]
    plt.bar(index,values)
    #Axes - это та область на которой чаще всего и отражаются графики (данные в виде графиков), а так же все вспомогательные атрибуты (линии сетки, метки, указатели и т.д.)
    ax = fig.add_subplot(111)

    """
                    # the figure that will contain the plot 
                    fig = Figure(figsize = (5, 5), dpi = 100) 
  
                    # list of squares 
                    y = [i**2 for i in range(101)] 
  
                    # adding the subplot 
                    plot1 = fig.add_subplot(111) 
  
                    # plotting the graph 
                    plot1.plot(y) 
    """

    # creating the Tkinter canvas 
    # containing the Matplotlib figure 
    canvas = FigureCanvasTkAgg(fig, 
                               master = window)   
    canvas.draw() 
  
    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().pack() 
  
    # creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, 
                                   window) 
    toolbar.update() 
  
    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().pack() 

# the main Tkinter window 
window = Tk() 

# setting the title  
window.title('Plotting in Tkinter')

# dimensions of the main window 
window.geometry("500x500") 

# button that displays the plot 
plot_button = Button(master = window,  
                     command = plot, 
                     height = 2,  
                     width = 10, 
                     text = "Plot")

# place the button  
# in main window 
plot_button.pack() 

# run the gui 
window.mainloop() 


"""
x = [1,1,2,3,3,5,7,8,9,10, 10,11,11,13,13,15,16,17,18,18]
plt.hist(x, bins=10)
#plt.show()
root = Tk()
root.title("Добро пожаловать в приложение PythonRu")
root.mainloop()
"""