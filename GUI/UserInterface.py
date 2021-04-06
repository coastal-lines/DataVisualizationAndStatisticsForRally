from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
import seaborn as sns
import mplcursors
import pandas as pd
from pyral import Rally, rallyWorkset
from CommonClass import CommonClass
from Visualization.UserDataObjects.UserTabData import UserTabData
from Visualization.DataFrameActions import DataFrameActions

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
        self.tabControl.place(x = 0, y = 0, width = 1800, height = 900)

        self.createMainTab()

        #endles loop for wait any user interactions - will works during window is opened
        self.window.mainloop()

    def createMainTab(self):
        tab = ttk.Frame()

        self.tabControl.add(tab, text ='Settings')
        #the main screen?!

        #query elements frame
        self.createQueryPanel(tab)

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

        labelExtendedMode = Label(master = tab, text="Extended mode:")
        labelExtendedMode.place(x = 0, y = 200, width=100)
        checkBoxVar = IntVar()
        checkBoxExtendedMode = Checkbutton(master = tab, text="Extended mode", variable=checkBoxVar)
        checkBoxExtendedMode.place(x = 0, y = 220, width=100)
        buttonLoadTestCases = Button(master = tab, text = "Download test cases from root folder", command = self.saveTestCasesIntoFile)
        buttonLoadTestCases.place(x = 100, y = 240, width=200)

        params = []
        with open(r'C:\Users\User\Desktop\!temp') as my_file:
            for line in my_file:
                params.append(line)

        self.serverText.insert(0, params[0].rstrip())
        self.userText.insert(0, params[1].rstrip())
        self.passwordText.insert(0, params[2].rstrip())
        self.workspaceText.insert(0, params[3].rstrip())
        self.projectText.insert(0, params[4].rstrip())
        self.rootFolderText.insert(0, params[5].rstrip()) #TF15961 
        self.queryText.insert(0, params[6].rstrip())
    
    def createTab(self):
        if self.queryText.get() == "":
            self.createDefaultTab()
        else:
            self.createCustomTab()

    def createCustomTab(self):
        query = self.queryText.get()
        tidy = self.commonClass.getCustomUserRequest(query, self.rootFolderText.get())

        #all test cases chart pie
        allTestCasesForChartPie = DataFrameActions.prepareDataForAllTestCasesChartPie(tidy)

        #specific test cases chart pie
        specificTestCasesDict = self.commonClass.getSpecificTestCasesForChartPie("user")

        self.tabCount = self.tabCount + 1

        #matplotlib frame 
        tab = ttk.Frame()
        tab.place(x = 0, y = 0)
        self.tabControl.add(tab, text = "User query")

        figureFrame = Frame(master = tab, width = 1600, height = 800, bg="red")
        figureFrame.place(x = 0, y = 0)

        dpi = 96
        plt.rcParams['figure.figsize']=(1520 / dpi, 760 / dpi)
        plt.rcParams.update({'figure.autolayout': True})
        fig, ax = plt.subplots()
        #set folder name for Figure
        fig.suptitle("User query: " + query)
        ax = sns.barplot(y='names', x='value', hue='variable', data = tidy)
        ax.set_xlim(0, max(tidy.value) + 1)
        ax.set_xticks(range(1, max(tidy.value) + 1))
        #??????????????
        canvas = FigureCanvasTkAgg(fig, master = figureFrame)
        canvas.draw()
        canvas.get_tk_widget().grid()

        self.listUserTabData.append(UserTabData(self.tabCount, None, None, None))
                
        #фрейм для авто/ручное
        self.createFullCountTestCasesPie(tab, allTestCasesForChartPie)
        self.createCustomPie1(tab, specificTestCasesDict)
        self.createCustomPie2(tab)

        figureToolbar = Frame(master = tab, width = 1600, height = 40, bg="black")
        figureToolbar.place(x = 0, y = 800)
        toolbar = NavigationToolbar2Tk(canvas, figureToolbar, pack_toolbar = False)
        toolbar.place(x = 0, y = 0)
        
        self.createQueryPanel(tab)
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
        self.commonClass.clearTestCasesFromUserQueryList()
        self.tidy = self.commonClass.getTidyData()
        self.unTidy = self.commonClass.getUntidyData()

        self.listUserTabData.append(UserTabData(self.tabCount, self.tidy, self.unTidy, self.rootFolderName))

        ax = sns.barplot(y='names', x='value', hue='variable', data = self.tidy)

        ax.set_xlim(0, max(self.tidy.value) + 1)
        ax.set_xticks(range(1, max(self.tidy.value) + 1))

        canvas = FigureCanvasTkAgg(fig, master=tab)
        canvas.draw()
        canvas.get_tk_widget().grid()

        #all test cases chart pie
        allTestCasesForChartPie = DataFrameActions.prepareDataForAllTestCasesChartPie(self.tidy)
        #фрейм для авто/ручное
        self.createFullCountTestCasesPie(tab, allTestCasesForChartPie)

        #specific test cases chart pie
        self.commonClass.setTestCasesFromUserQuery()
        specificTestCasesDict = self.commonClass.getSpecificTestCasesForChartPie("default")
        self.createCustomPie1(tab, specificTestCasesDict)

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

    def createQueryPanel(self, tab):
        #query elements frame
        frameQueryElements = Frame(master = tab, width = 1800, height = 30)
        frameQueryElements.place(x = 0, y = 840)

        lbl = Label(master = frameQueryElements, text="Query input:")
        lbl.place(x = 0, y = 0, width=100)
        self.queryText = Entry(master = frameQueryElements)
        self.queryText.place(x = 100, y = 0, width=900, height = 22)
        btn = Button(master = frameQueryElements, text = "Find test cases", command = self.createTab)
        btn.place(x = 1000, y = 0, width=92)

    def createFullCountTestCasesPie(self, tab, allTestCasesForChartPie):
        #фрейм для авто/ручное
        totalTestCasesCountFrame = Frame(master = tab, width = 200, height = 200, bg="green")
        totalTestCasesCountFrame.place(x = 1600, y = 0)
        labels = 'Manual', 'AT'
        values = [allTestCasesForChartPie["manual"], allTestCasesForChartPie["automated"]]
        fig2, ax2 = plt.subplots()
        ax2.pie(values, labels=labels, autopct = lambda p: '{:.0f}'.format(p * sum(values) / 100), shadow=True, startangle=90, radius=800)
        ax2.axis('equal')
        fig2.set_size_inches(2,2)
        canvas2 = FigureCanvasTkAgg(fig2, master = totalTestCasesCountFrame)
        canvas2.draw()
        canvas2.get_tk_widget().grid()

    def createCustomPie1(self, tab, specificTestCasesDict):
        #фрейм для авто/ручное
        totalTestCasesCountFrame = Frame(master = tab, width = 200, height = 200, bg="green")
        totalTestCasesCountFrame.place(x = 1600, y = 210)
        labels = 'other', 'SC'
        values = [specificTestCasesDict["Other"], specificTestCasesDict["SC"]]
        fig2, ax2 = plt.subplots()
        ax2.pie(values, labels=labels, autopct = lambda p: '{:.0f}'.format(p * sum(values) / 100), shadow=True, startangle=90, radius=800)
        ax2.axis('equal')
        fig2.set_size_inches(2,2)
        canvas2 = FigureCanvasTkAgg(fig2, master = totalTestCasesCountFrame)
        canvas2.draw()
        canvas2.get_tk_widget().grid()

    def createCustomPie2(self, tab):
        #фрейм для авто/ручное
        totalTestCasesCountFrame = Frame(master = tab, width = 200, height = 200, bg="green")
        totalTestCasesCountFrame.place(x = 1600, y = 400)
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

    def prepareAbsoluteValuesForChartPie(values):
        a  = numpy.round(values/100.*sizes.sum(), 0)
        return a
        
    def saveTestCasesIntoFile(self):
        self.commonClass.downloadAllTestCasesIntoFileForExtendedMode()