import requests
import pickle
from pyral import Rally, rallyWorkset
import matplotlib.pyplot as plt
from matplotlib import pylab
import seaborn as sns
from pylab import *
from matplotlib.ticker import MaxNLocator
import mplcursors
import pandas as pd
from Project.RallyCommonObject import RallyCommonObject
from Project.UserCredential import UserCredential
from Project.RallyInstance import RallyInstance
from Project.RallyFolder import RallyFolder
from Project.RallyWorkspace import RallyWorkspace
from Visualization.UserDataObjects.BarClass import BarClass
from Visualization.TestsAndFoldersActions import TestsAndFoldersActions
from Visualization.DataFrameActions import DataFrameActions

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
    allTestCasesForSaveIntoFile = None

    def login(self, server, login, password):
        self.user = UserCredential(server, login, password)
        self.rally = RallyInstance(self.user).rally

    def startSession(self, workspace, project, folder):
        try:
            self.rally.setWorkspace(workspace)
            self.rally.setProject(project)
            self.rootFolder = RallyFolder(self.rally ,'FormattedID = "' + folder + '"').testFolder
        except:
            print("Please login before")

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

    def downloadAllTestCasesIntoFileForExtendedMode(self):
        self.allTestCasesForSaveIntoFile = TestsAndFoldersActions().extractTestCasesFromFoldersAndSubfolders(self.rootFolder)
        with open(r'C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\listTestCases.data', 'w+b') as file:
            pickle.dump(listTC, file)
    
    def getAllTestCasesForSaveIntoFile(self):
        return self.allTestCasesForSaveIntoFile