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
rootFolderId = "TF15961"

rally = Rally(server=server, user=user, password=password)
rally.setWorkspace(workspace)
rally.setProject(project)

rootFolder = RallyFolder(rally ,'FormattedID = ' + rootFolderId).testFolder
mainFolderName = rootFolder.Name
mainFolderChildren = rootFolder.Children

listTC = []
params = []

query = 'FormattedID = ' + rootFolderId
#query = 'FormattedID = "TF23805" AND FormattedID = "TF18607"'
test_folder_req = rally.get('TestFolder', fetch=True, projectScopeDown=True, query=query)
test_folder = test_folder_req.next()
test_cases = test_folder.TestCases

for tc in test_cases:
    listTC.append(tc)