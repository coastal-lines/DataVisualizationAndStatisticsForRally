from DataVisualization.Visualization.UserDataObjects.BarClass import BarClass
from DataVisualization.Visualization.UserDataObjects.UserTestFromRequest import UserTestFromRequest
from DataVisualization.Visualization.UserDataObjects.UserTestFromRequest import UserTestFromRequest
from DataVisualization.Project.RallyFolder import RallyFolder
from pyral import Rally, rallyWorkset

class TestsAndFoldersActions():
    allTestCasesInFolderIncludeSubfolders = []
    allTC = []
    listTC = []

    #def __init__(self, allTestCasesInFolderIncludeSubfolders, rootFolder):
     #   self.rootFolder = rootFolder

    @staticmethod
    def extractFoldersFromRootFolder(rootFolder):
        listBars = []
        folderNumber = 0
        #first iteration
        #if folder has testcases
        if len(rootFolder.TestCases) > 0:
            folderNumber = folderNumber + 1
            TestsAndFoldersActions.extractTestCasesFromRootFolder(rootFolder)
            tcDict = TestsAndFoldersActions.prepareDict()
            listBars.append(BarClass(rootFolder.Name, rootFolder.FormattedID, tcDict["manual"], tcDict["automated"]))
            TestsAndFoldersActions.allTestCasesInFolderIncludeSubfolders.clear()

        if len(rootFolder.Children) > 0:
            for folder in rootFolder.Children:
                folderNumber = folderNumber + 1
                TestsAndFoldersActions.extractTestCasesFromFolder(folder)
                tcDict = TestsAndFoldersActions.prepareDict()
                #listBars.append(BarClass(folderNumber, tcDict["manual"], tcDict["automated"], folder.Name))
                listBars.append(BarClass(folder.Name, folder.FormattedID, tcDict["manual"], tcDict["automated"]))
                TestsAndFoldersActions.allTestCasesInFolderIncludeSubfolders.clear()

        return listBars

    @staticmethod
    def extractFolders(folders):
        for folder in folders:
            print(folder.Name)
            print("---")
            TestsAndFoldersActions.extractTestCasesFromFolder(folder)

    @staticmethod
    def extractTestCasesFromFolder(folder):
        if len(folder.TestCases) > 0:
            for testCase in folder.TestCases: 
                print(testCase.Name)
                TestsAndFoldersActions.allTestCasesInFolderIncludeSubfolders.append(testCase)
                TestsAndFoldersActions.allTC.append(testCase)
        if len(folder.Children) > 0:
            TestsAndFoldersActions.extractFolders(folder.Children)

    @staticmethod
    def extractTestCasesFromRootFolder(folder):
        if len(folder.TestCases) > 0:
            for testCase in folder.TestCases: 
                print(testCase.Name)
                TestsAndFoldersActions.allTestCasesInFolderIncludeSubfolders.append(testCase)
                TestsAndFoldersActions.allTC.append(testCase)

    #@staticmethod
    def prepareDict():
        m = 0
        a = 0

        if len(TestsAndFoldersActions.allTestCasesInFolderIncludeSubfolders) > 0:
            for testCase in TestsAndFoldersActions.allTestCasesInFolderIncludeSubfolders:
                if testCase.Name.find("[AUTOMATED]") != -1:
                    a = a + 1
                else:
                    m = m + 1
        testCasesDict = dict(manual = m, automated = a)
        return testCasesDict

    @staticmethod
    def getMaxValueTestCases(bars):
        manual = []
        automated = []
        for bar in bars:
            manual.append(bar.countManualTestCases)
            automated.append(bar.countAutomatedTestCases)

        countTestCases = manual + automated
        maxAxisX = max(countTestCases) + 1
        return maxAxisX

    @staticmethod
    def getCustomUserRequest(testCasesFromUserQuery, listRootSubfolders):
        #extract test cases from response
        #listTC = []
        for number in range(testCasesFromUserQuery.resultCount):
            TestsAndFoldersActions.listTC.append(testCasesFromUserQuery.next())

        #prepare cases for bars
        listRootFoldersOfUser = []
        for tc in TestsAndFoldersActions.listTC:
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
                    tcRoot = TestsAndFoldersActions.getParentName(tf, rootFolder.Name)
                    #break

            #add to list
            listRootFoldersOfUser.append(UserTestFromRequest(tcRoot, tcType, tcName, tcId))

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

            #listUserBars.append(UserSpecialBar(name, manual, automated))
            listUserBars.append(BarClass(name, "-1", manual, automated))

        #ids = []
        names = []
        manual = []
        automated = []

        for item in listUserBars:
            #names.append(item.name)
            #manual.append(item.manual)
            #automated.append(item.automated)
            names.append(item.headFolderdName)
            manual.append(item.countManualTestCases)
            automated.append(item.countAutomatedTestCases)

        return listUserBars

    #find parent name by recursion
    @classmethod
    def getParentName(cls, testFolder, rootFolderName):
        try:
            if testFolder.Name != None and testFolder.Name == rootFolderName:
                return rootFolderName
            else:
                TestsAndFoldersActions.getParentName(testFolder.Parent, rootFolderName)
        except AttributeError:
            print("not this root folder")

    #надо переименовать
    @staticmethod
    def getDataForCustomChartPie1(testCasesFromUserQuery, typeOfRequest):
        countSpecificTestCases = 0
        countAllOtherTestCases = 0

        if typeOfRequest == "user":
            countAllOtherTestCases = len(TestsAndFoldersActions.listTC)
            for testCase in TestsAndFoldersActions.listTC:
                if "SecureClient" in testCase.Name or "Secure Client" in testCase.Name or "HTML SC" in testCase.Name:
                    countSpecificTestCases = countSpecificTestCases + 1

        if typeOfRequest == "default":
            for testCase in testCasesFromUserQuery:
                countAllOtherTestCases = countAllOtherTestCases + 1
                if "SecureClient" in testCase.Name or "Secure Client" in testCase.Name or "HTML SC" in testCase.Name:
                    countSpecificTestCases = countSpecificTestCases + 1

        countAllOtherTestCases = countAllOtherTestCases - countSpecificTestCases
        specificTestCasesDict = {"SC": countSpecificTestCases, "Other": countAllOtherTestCases}

        return specificTestCasesDict

    @staticmethod
    def getAllTestCasesInFolderIncludeSubfolders():
        return TestsAndFoldersActions.allTC