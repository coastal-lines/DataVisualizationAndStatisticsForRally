from pyral import Rally, rallyWorkset
import pickle
from Project.RallyFolder import RallyFolder

class TestCase():
    def __init__(self,mainFolderName, rootFolderName, formattedID, name, preConditions, productArea, productSubarea, method, testFolder, inputs, expecteds):
        self.mainFolderName = mainFolderName
        self.rootFolderName = rootFolderName
        self.formattedID = formattedID
        self.name = name
        self.preConditions = preConditions
        self.project = project
        self.productArea = productArea
        self.productSubarea = productSubarea
        self.method = method
        self.testFolder = testFolder
        self.inputs = inputs
        self.expecteds = expecteds

params = []

with open(r'C:\Users\User\Desktop\!temp') as my_file:
    for line in my_file:
        params.append(line)

server = params[0].rstrip()
user = params[1].rstrip()
password = params[2].rstrip()
workspace = params[3].rstrip()
project = params[4].rstrip()
#rootFolder = 'TF15963'
rootFolderId = "TF15961"

rally = Rally(server=server, user=user, password=password)
rally.setWorkspace(workspace)
rally.setProject(project)

rootFolder = RallyFolder(rally ,'FormattedID = ' + rootFolderId).testFolder
mainFolderName = rootFolder.Name
mainFolderChildren = rootFolder.Children

listTC = []
params = []

query = 'FormattedID = "TF16509"'
#query = 'FormattedID = "TF23805" AND FormattedID = "TF18607"'
test_folder_req = rally.get('TestFolder', fetch=True, projectScopeDown=True, query=query)
test_folder = test_folder_req.next()
test_cases = test_folder.TestCases

for tc in test_cases:
    listTC.append(tc)

with open(r'C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\listTestCases3.data', 'w+b') as file:
    pickle.dump(listTC, file)

with open(r'C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\listTestCases.data', 'rb') as file:
    l = pickle.load(file)
    t=0

count = 0 #debug
#предварительно узнаем имя корневой папки
rootFolder = RallyFolder(self.rally ,'FormattedID = "' + folderID + '"').testFolder

def getTestCaseParent(testCaseId):
    tc = rally.get('TestCase', fetch = True, projectScopeDown = True, query = 'FormattedID = ' + testCaseId + "'")
    d=0

for tc in test_cases:
    count = count + 1 #debug
    print(str(count) + ": " + tc.Name) #debug
    formattedID = tc.FormattedID
    name = tc.Name
    preConditions = tc.PreConditions
    productArea = tc.c_ProductArea
    productSubarea = tc.c_ProductSubarea
    method = tc.Method
    testFolder = tc.TestFolder.Name
    mainFolderName = mainFolderName
    rootFolderName = None

    #root
    for rootFolder in mainFolderChildren:
        if tc.testFolder.Name == rootFolder.Name:
            rootFolderName = rootFolder.Name
            break
        elif tc.TestFolder.Parent.Name == rootFolder.Name:
            tcRoot = tc.TestFolder.Parent.Name
            break
        else:
            tf = tc.TestFolder.Parent
            tcRoot = TestsAndFoldersActions.getParentName(tf, rootFolder.Name)
            #break

    inputs  = []
    expecteds = []

    list_steps = tc.Steps
    for i in list_steps:
        inputs.append(i.Input)
        expecteds.append(i.ExpectedResult)

    listTC.append(TestCase(formattedID, name, preConditions, productArea, productSubarea, method, testFolder, inputs, expecteds))



with open(r'C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\listTestCases2.data', 'w+b') as file:
    pickle.dump(listTC, file)

with open(r'C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\listTestCases.data', 'rb') as file:
    l = pickle.load(file)
    t=0

a = 0