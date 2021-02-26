import requests
from pyral import Rally, rallyWorkset
import matplotlib.pyplot as plt
from matplotlib import pylab
import seaborn as sns
from pylab import *
from matplotlib.ticker import MaxNLocator
import mplcursors
import pandas as pd
from DataVisualization.Project.RallyCommonObject import RallyCommonObject
from DataVisualization.Project.UserCredential import UserCredential
from DataVisualization.Project.RallyInstance import RallyInstance
from DataVisualization.Project.RallyFolder import RallyFolder
from DataVisualization.Project.RallyWorkspace import RallyWorkspace
from DataVisualization.Visualization.UserDataObjects.BarClass import BarClass
from DataVisualization.Visualization.TestsAndFoldersActions import TestsAndFoldersActions
from DataVisualization.Visualization.DataFrameActions import DataFrameActions

class UserSpecialBar():
    def __init__(self, name, manual, automated):
        self.name = name
        self.manual = manual
        self.automated = automated

class UserTestFromRequest():
    def __init__(self, rootFolder, tcType, name, id):
        self.rootFolder = rootFolder
        self.tcType = tcType
        self.name = name
        self.id = id

class CommonClass():
    rally = None
    totalTestsCount = 0
    totalManualTestsCount = 0
    totalAutomatedTestsCount = 0
    tabCount = 0
    rootFolder = None
    tidyDataForCustomUserQuery = None
    testCasesFromUserQuery = None

    def login(self, server, login, password):
        self.user = UserCredential(server, login, password)
        self.rally = RallyInstance(self.user).rally

    def startSession(self, workspace, project, folder):
        self.rally.setWorkspace(workspace)
        self.rally.setProject(project)
        self.rootFolder = RallyFolder(self.rally ,'FormattedID = "' + folder + '"').testFolder
        x = 100

    def getRootFolderName(self):
        return self.rootFolder.Name

    def getTidyData(self):
        bars = TestsAndFoldersActions().extractFoldersFromRootFolder(self.rootFolder)
        tidyData = DataFrameActions.PrepareDataFrame(bars)
        return tidyData

    def getUntidyData(self):
        return DataFrameActions.getDataFrame()

    def setRootFolder(self, folderID):
        self.rootFolder = RallyFolder(self.rally ,'FormattedID = "' + folderID + '"').testFolder

    def getCustomUserRequest(self, query, rootFolderFormattedID):
        #get response with User's query
        self.testCasesFromUserQuery = self.rally.get('TestCase', fetch = True, projectScopeDown = True, query = query)

        #get root test folders according the main root folder
        rootFolder = RallyFolder(self.rally ,'FormattedID = "' + rootFolderFormattedID + '"').testFolder
        listRootSubfolders = rootFolder.Children

        bars = TestsAndFoldersActions().getCustomUserRequest(self.testCasesFromUserQuery, listRootSubfolders)
        tidyDataForCustomUserQuery = DataFrameActions.PrepareDataFrame(bars)

        return tidyDataForCustomUserQuery

    def setTestCasesFromUserQuery(self):
        self.testCasesFromUserQuery = TestsAndFoldersActions().getAllTestCasesInFolderIncludeSubfolders()

    def getSpecificTestCasesForChartPie(self, typeOfRequest):
        #SC and other
        specificTestCasesDict = TestsAndFoldersActions().getDataForCustomChartPie1(self.testCasesFromUserQuery, typeOfRequest)

        return specificTestCasesDict