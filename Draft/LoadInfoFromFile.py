import pickle
import re

class TestCase():
    def __init__(self, formattedID, name, preConditions, productArea, productSubarea, method, testFolder, inputs, expecteds):
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

userTestCasesFromFile = None
with open(r'C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\listTestCases2.data', 'rb') as file:
    userTestCasesFromFile = pickle.load(file)

query = '(Name contains "material")'
query = '((Name contains "material") AND (PreConditions contains "subjec"))'
what = None
how = None
where = None

result = re.findall('\((.*?)\)', query)
selectedUserTestCases = []

userTestCasesFromFileCopy = userTestCasesFromFile.copy()
#pre-removing test cases
for query in result:
    what = query.split()[0]
    action =  query.split()[1]
    text = query.split()[2]
    if(action == "!contains" or action == "!="):
        removeTestCasesFromList()

def removeTestCasesFromList(what, text):
    for tc in userTestCasesFromFile:
        if what == "Name":
            pass
        elif what == "PreCondition":
            pass
        elif what == "Project":
            pass
        elif what == "":
            pass
        elif what == "":
            pass
        elif what == "":
            pass
        elif what == "":
            pass
        elif what == "":
            pass
        elif what == "":
            pass

for query in result:
    what = query.split()[0]
    action =  query.split()[1]
    text = query.split()[2]



    for tc in userTestCasesFromFile:
        if where == "Name":
            pass

def findByName(action, text):
    if "contains" in action:
        for tc in userTestCasesFromFile:
            if text in tc.name:
                selectedUserTestCases.append(tc)

    if "=" in action:
        for tc in userTestCasesFromFile:
            if text == tc.name:
                selectedUserTestCases.append(tc)