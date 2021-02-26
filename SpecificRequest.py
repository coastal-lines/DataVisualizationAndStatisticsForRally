import requests
from pyral import Rally, rallyWorkset
import matplotlib.pyplot as plt
from DataVisualization.Project.RallyFolder import RallyFolder
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
import seaborn as sns
from tkinter import *
from tkinter import ttk

class UserTestFromRequest():
    def __init__(self, rootFolder, tcType, name, id):
        self.rootFolder = rootFolder
        self.tcType = tcType
        self.name = name
        self.id = id

class UserSpecialBar():
    def __init__(self, name, manual, automated):
        self.name = name
        self.manual = manual
        self.automated = automated

listUserTestFromRequest = []


testFolderChildrens = None
rally = None

def login():
    rally = Rally(server=server, user=user, password=password)

    workspaces = rally.getWorkspaces()

    rootWorkspace = None
    for ws in workspaces:
        if(ws.Name == 'БТЛ Group Ltd.'):
            rootWorkspace = ws
            break

    projects = rally.getProjects(workspace=rootWorkspace.Name)
    rootProject = None


    for pr in projects:
        print(pr.Name)
        if(pr.Name == 'Сурпас 12 Regression Тест Pack'):
            print(pr);
            rootProject = pr
            break

    rally.setWorkspace(rootWorkspace.Name)
    rally.setProject(rootProject.Name)

    #rootFolder = RallyFolder(rally ,'FormattedID = "' + 'TF15719' + '"').testFolder
    #tt= 200

    query = 'Name CONTAINS "HTML Деливери (browser-based) - Allow"'
    tcs = rally.get('TestCase', fetch=True, projectScopeDown=True, query=query)

    #get user cases
    listTC = []
    for number in range(tcs.resultCount):
        listTC.append(tcs.next())

    #get root folders
    rootFolder = RallyFolder(rally ,'FormattedID = "' + 'ТФ15961' + '"').testFolder
    listRootSubfolders = rootFolder.Children

    #prepare cases for bars
    listRootFoldersOfUser = []
    for tc in listTC:
        tcType = None
        tcId = None
        tcRoot = None
        tcName = None

        #name
        tcName = tc.Name

        #id
        tcId = tc.FormattedID

        #type
        if tc.Name.find("AUTOMATED") != -1:
            tcType = "automated"
        else:
            tcType = "manual"

        #root
        for rootFolder in listRootSubfolders:
            if tc.TestFolder.Name == rootFolder.Name:
                tcRoot = rootFolder.Name
                break
            elif tc.TestFolder.Parent.Name == rootFolder.Name:
                tcRoot = tc.TestFolder.Parent.Name
                break
            else:
                tf = tc.TestFolder.Parent
                tcRoot = getParentName(tf, rootFolder.Name)
                #break

        #add to list
        listRootFoldersOfUser.append(UserTestFromRequest(tcRoot, tcType, tcName, tcId))
    prepareForMatPlotLib(listRootFoldersOfUser)

def prepareForMatPlotLib(listRootFoldersOfUser):
    #uniq root folders
    uniqRootFolders = list(set([tc.rootFolder for tc in listRootFoldersOfUser]))

    #for each uniq folder how many manual and auto tests
    listUserBars = []
    for unRoot in uniqRootFolders:
        manual = 0
        automated = 0
        name = unRoot

        for item in listRootFoldersOfUser:
            if unRoot == item.rootFolder:
                if item.tcType == "manual":
                    manual = manual + 1
                else:
                    automated = automated + 1

        listUserBars.append(UserSpecialBar(name, manual, automated))
    t = 100
    createTab(listUserBars)

def createTab(listUserBars):
    #matplotlib frame 
    """
        tab = ttk.Frame()

        tabControl = ttk.Notebook(window)
        tabControl.add(tab, text = 'Custom query')
        tabControl.place(x = 0, y = 0)

        canvas = Canvas(master = tab, width = 1600, height = 800)
        canvas.place(x = 0, y = 0)
    """

    dpi = 96
    plt.rcParams['figure.figsize']=(1550 / dpi, 750 / dpi)
    plt.rcParams.update({'figure.autolayout': True})

    fig, axs = plt.subplots()

    #set folder name for Figure
    fig.suptitle('Custom query: ' + 'Name CONTAINS "HTML Деливери (browser-based) - Allow')

    #get tidy data
    names = []
    manual = []
    automated = []

    for item in listUserBars:
        names.append(item.name)
        manual.append(item.manual)
        automated.append(item.automated)

    dataFrame = pd.DataFrame({
        'ids': None,
        'names': names,
        'manual': manual,
        'automated': automated
    })

    tidy = dataFrame.melt(id_vars='names', value_vars=['manual', 'automated'])

    #calculate full count cases
    totalTestsCount = 0
    totalManualTestsCount = 0
    totalAutomatedTestsCount = 0
    for item in tidy.values:
        if item[1] == "manual":
            totalTestsCount = totalTestsCount + int(item[2])
            totalManualTestsCount = totalManualTestsCount + int(item[2])
        else:
            totalTestsCount = totalTestsCount + int(item[2])
            totalAutomatedTestsCount = totalAutomatedTestsCount + int(item[2])

    sns.barplot(y='names', x='value', hue='variable', data = tidy, ax=axs[0])

    axs[0].set_xlim(0, max(tidy.value) + 1)
    axs[0].set_xticks(range(1, max(tidy.value) + 1))
    """
        canvas = FigureCanvasTkAgg(fig, master=tab)
        canvas.draw()
        canvas.get_tk_widget().grid()

        toolbar = NavigationToolbar2Tk(canvas, tab, pack_toolbar=False)
        toolbar.place(x = 0, y = 780)
    """

    """
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)
    axs[1].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    axs[1].axis('equal')
    """

    plt.show()

def getParentName(tf, rootName):
    try:
        if tf.Name != None and tf.Name == rootName:
            return rootName
        else:
            getParentName(tf.Parent, rootName)
    except AttributeError:
        print("not this root folder")


login()
