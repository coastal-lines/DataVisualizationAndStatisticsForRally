from tkinter import *  
from tkinter import ttk  

def addTab():
    tab_control = ttk.Notebook(frameCanvas)  
    tab1 = Frame(frameCanvas)  
    tab_control.add(tab1, text='Первая')  
    tab_control.pack(expand=0, fill='both')  

window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('400x250')

frameCanvas = Frame(window, width = 800, height = 800, bg="white")
frameCanvas.place(x = 0, y = 0)

btn = Button(master = window, text = "Add tab", command = addTab)
btn.place(x = 0, y = 350, width=100)

window.mainloop()