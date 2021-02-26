from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
import seaborn as sns
import mplcursors
import pandas as pd
from pyral import Rally, rallyWorkset
from DataVisualization.CommonClass import CommonClass
from DataVisualization.Visualization.UserDataObjects.UserTabData import UserTabData

class UserInterface():
    tabCount = 0
    tabControl = None
    queryText = None
    commonClass = CommonClass()
    tidy = None
    unTidy = None
    rootFolderName = None
    listUserTabData = []
    window = None

    def createWindow(self):        
        
        self.window = Tk()

        #title
        self.window.title("Rally Data Visualization and Prediction")
        self.window.geometry("1800x900")

        self.tabControl = ttk.Notebook(self.window)
        self.tabControl.place(x = 0, y = 0, width = 1800, height = 800)

        self.createMainTab()

        #endles loop for wait any user interactions - will works during window is opened
        self.window.mainloop()

    def createMainTab(self):
        tab = ttk.Frame()

        self.tabControl.add(tab, text ='Settings')
        #the main screen?!

        #query elements frame
        frameQueryElements = Frame(master = self.window, width = 1800, height = 20)
        frameQueryElements.place(x = 0, y = 800)

        lbl = Label(master = frameQueryElements, text="Query input:")
        lbl.place(x = 0, y = 0, width=100)
        self.queryText = Entry(master = frameQueryElements)
        self.queryText.place(x = 100, y = 0, width=900)
        btn = Button(master = frameQueryElements, text = "Find test cases", command = self.createTab)
        btn.place(x = 1000, y = 0, width=92)
        

        lbl1 = Label(master = tab, text="Server:")
        lbl1.place(x = 0, y = 0, width=100)
        self.serverText = Entry(master = tab)
        self.serverText.place(x = 100, y = 0, width=200)
        lbl2 = Label(master = tab, text="User:")
        lbl2.place(x = 0, y = 20, width=100)
        self.userText = Entry(master = tab)
        self.userText.place(x = 100, y = 20, width=200)
        lbl3 = Label(master = tab, text="Password:")
        lbl3.place(x = 0, y = 40, width=100)
        self.passwordText = Entry(master = tab)
        self.passwordText.place(x = 100, y = 40, width=200)
        btnLogin = Button(master = tab, text = "Login", command = self.login)
        btnLogin.place(x = 100, y = 60, width=200)

        lbl4 = Label(master = tab, text="Workspace:")
        lbl4.place(x = 0, y = 100, width=100)
        self.workspaceText = Entry(master = tab)
        self.workspaceText.place(x = 100, y = 100, width=200)
        lbl5 = Label(master = tab, text="Project:")
        lbl5.place(x = 0, y = 120, width=100)
        self.projectText = Entry(master = tab)
        self.projectText.place(x = 100, y = 120, width=200)
        lbl6 = Label(master = tab, text="Root folder:")
        lbl6.place(x = 0, y = 140, width=100)
        self.rootFolderText = Entry(master = tab)
        self.rootFolderText.place(x = 100, y = 140, width=200)
        btnSetWorkspace = Button(master = tab, text = "Start session", command = self.startSession)
        btnSetWorkspace.place(x = 100, y = 160, width=200)
    
    def createTab(self):
        if self.queryText.get() == "":
            self.createDefaultTab()
        else:
            self.createCustomTab()

    def createCustomTab(self):
        query = self.queryText.get()
        #tidy = self.commonClass.getCustomUserRequest(query, self.rootFolderText.get())
        tidy = self.tempTidy()

        self.tabCount = self.tabCount + 1

        #matplotlib frame 
        tab = ttk.Frame()
        tab.place(x = 0, y = 0)
        self.tabControl.add(tab, text = "User query")

        figureFrame = Frame(master = tab, width = 1600, height = 700, bg="red")
        figureFrame.place(x = 0, y = 0)
        
        dpi = 96
        plt.rcParams['figure.figsize']=(1450 / dpi, 550 / dpi)
        plt.rcParams.update({'figure.autolayout': True})

        fig, ax = plt.subplots()
        
        #set folder name for Figure
        fig.suptitle("User query: " + query)

        self.listUserTabData.append(UserTabData(self.tabCount, None, None, None))

        ax = sns.barplot(y='names', x='value', hue='variable', data = tidy)

        ax.set_xlim(0, max(tidy.value) + 1)
        ax.set_xticks(range(1, max(tidy.value) + 1))
        
        #??????????????
        canvas = FigureCanvasTkAgg(fig, master = figureFrame)
        canvas.draw()
        canvas.get_tk_widget().grid()
        
        figureToolbar = Frame(master = tab, width = 1600, height = 40, bg="red", relief=RIDGE)
        figureToolbar.place(x = 0, y = 800)
        toolbar = NavigationToolbar2Tk(canvas, figureToolbar, pack_toolbar = False)
        toolbar.place(x = 0, y = 0)

        #фрейм для авто/ручное
        totalTestCasesCountFrame = Frame(master = tab, width = 200, height = 200, bg="green")
        totalTestCasesCountFrame.place(x = 1600, y = 30)
        labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
        sizes = [15, 30, 45, 10]
        explode = (0, 0.1, 0, 0)
        fig2, ax2 = plt.subplots()
        ax2.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, radius=800)
        ax2.axis('equal')
        fig2.set_size_inches(2,2)
        canvas2 = FigureCanvasTkAgg(fig2, master = totalTestCasesCountFrame)
        canvas2.draw()
        canvas2.get_tk_widget().grid()
        
        #self.tempCreate(tab)

    def createDefaultTab(self):
        self.tabCount = self.tabCount + 1

        #matplotlib frame 
        tab = ttk.Frame()

        #get root folder name
        self.rootFolderName = self.commonClass.getRootFolderName()

        #self.tabControl.add(tab, text ='Tab ' + str(self.tabCount))
        self.tabControl.add(tab, text = self.rootFolderName)
        #self.tabControl.place(x = 0, y = 0)

        #?????????????????????
        #canvas = Canvas(master = tab, width = 1600, height = 800)
        #canvas.place(x = 0, y = 0)

        dpi = 96
        plt.rcParams['figure.figsize']=(1450 / dpi, 750 / dpi)
        plt.rcParams.update({'figure.autolayout': True})

        fig, ax = plt.subplots()

        #set folder name for Figure
        fig.suptitle(self.rootFolderName)

        #get tidy data
        self.tidy = self.commonClass.getTidyData()
        self.unTidy = self.commonClass.getUntidyData()

        self.listUserTabData.append(UserTabData(self.tabCount, self.tidy, self.unTidy, self.rootFolderName))

        ax = sns.barplot(y='names', x='value', hue='variable', data = self.tidy)

        ax.set_xlim(0, max(self.tidy.value) + 1)
        ax.set_xticks(range(1, max(self.tidy.value) + 1))

        canvas = FigureCanvasTkAgg(fig, master=tab)
        canvas.draw()
        canvas.get_tk_widget().grid()

        toolbar = NavigationToolbar2Tk(canvas, tab, pack_toolbar=False)
        toolbar.place(x = 0, y = 780)

        mplcursors.cursor(ax, hover=False).connect("add", lambda sel: sel.annotation.set_text(self.openNextTabByUserSelecting(sel.target.index)))

    def login(self):
        self.commonClass.login(self.serverText.get(), self.userText.get(), self.passwordText.get())

    def startSession(self):
        self.commonClass.startSession(self.workspaceText.get(), self.projectText.get(), self.rootFolderText.get())

    def openNextTabByUserSelecting(self, index):
        print("bar is: " + str(index))

        #need to use current tab's data - at this monent there are data just from the last tab
        #if current = actual => don't override
        allTabs = self.tabControl.tabs()
        cTab = self.tabControl.select()
        currentTab = self.tabControl.nametowidget(cTab)
        cName = currentTab._name
        currentTabIndex = allTabs.index("." + cName)
        self.rootFolderName = self.listUserTabData[currentTabIndex - 1].rootFolderName
        self.tidy = self.listUserTabData[currentTabIndex - 1].tidyData
        self.unTidy = self.listUserTabData[currentTabIndex - 1].untidyData

        #override rootFolder
        #don't open new tab if folder has only test cases
        if int((len(self.tidy.names) / 2)) > 1:
            newFolderId = self.unTidy.ids[index]
            self.commonClass.setRootFolder(newFolderId)
            self.createTab()

    def createPieForAllTestCases(self):
        pass

    def tempCreate(self, tab):
        #фрейм для авто/ручное
        totalTestCasesCountFrame = Frame(master = tab, width = 200, height = 200, bg="red")
        totalTestCasesCountFrame.place(x = 1500, y = 30)
        labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
        sizes = [15, 30, 45, 10]
        explode = (0, 0.1, 0, 0)
        fig2, ax2 = plt.subplots()
        ax2.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, radius=800)
        ax2.axis('equal')
        fig2.set_size_inches(2,2)
        canvas2 = FigureCanvasTkAgg(fig2, master = totalTestCasesCountFrame)
        canvas2.draw()
        canvas2.get_tk_widget().grid()

    def tempTidy(self):
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

        tidy = df.melt(id_vars='names', value_vars=['manual', 'automated'])
        return tidy