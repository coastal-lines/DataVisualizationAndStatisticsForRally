import tkinter as tk                     
from tkinter import ttk 
  
def addTab():
    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab2, text ='Tab 2') 
    ttk.Label(tab2, 
          text ="Lets dive into the\ world of computers").grid(column = 0, 
                                    row = 0,  
                                    padx = 30, 
                                    pady = 30) 
  
root = tk.Tk() 
root.title("Tab Widget") 
tabControl = ttk.Notebook(root) 
  
tab1 = ttk.Frame(tabControl) 
tabControl.add(tab1, text ='Tab 1')
tabControl.place(x = 0, y = 0)
ttk.Label(tab1, text ="Welcome to \  GeeksForGeeks").grid(column = 0,  
                               row = 0, 
                               padx = 30, 
                               pady = 30)   

btn = ttk.Button(root, text = "Find test cases", command = addTab)
btn.place(x = 0, y = 300, width=92)

root.mainloop()