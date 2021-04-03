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

query = '(Name !contains "Flash")'
#query = '((Name contains "material") AND (PreConditions contains "subjec"))'

result = re.findall('\((.*?)\)', query)
selectedUserTestCases = []

userTestCasesFromFileCopy = userTestCasesFromFile.copy()

def removeTestCasesFromList(what, text):
    for tc in userTestCasesFromFile:
        if what == "Name":
            for tc in userTestCasesFromFileCopy:
                if text in tc.name:
                    index = userTestCasesFromFileCopy.index(tc)
                    userTestCasesFromFileCopy.pop(index)
                break
            break
        elif what == "PreCondition":
            for tc in userTestCasesFromFileCopy:
                if text in tc.preConditions:
                    index = userTestCasesFromFileCopy.index(tc)
                    userTestCasesFromFileCopy.pop(index)
                break
        elif what == "Project":
            for tc in userTestCasesFromFileCopy:
                if text in tc.project:
                    index = userTestCasesFromFileCopy.index(tc)
                    userTestCasesFromFileCopy.pop(index)
                break
            break
        elif what == "ProductArea":
            for tc in userTestCasesFromFileCopy:
                if text in tc.productArea:
                    index = userTestCasesFromFileCopy.index(tc)
                    userTestCasesFromFileCopy.pop(index)
                break
            break
        elif what == "ProductSubarea":
            for tc in userTestCasesFromFileCopy:
                if text in tc.productSubarea:
                    index = userTestCasesFromFileCopy.index(tc)
                    userTestCasesFromFileCopy.pop(index)
                break
            break
        elif what == "Method":
            for tc in userTestCasesFromFileCopy:
                if text in tc.method:
                    index = userTestCasesFromFileCopy.index(tc)
                    userTestCasesFromFileCopy.pop(index)
                break
            break
        elif what == "TestFolder":
            for tc in userTestCasesFromFileCopy:
                if text in tc.testFolder:
                    index = userTestCasesFromFileCopy.index(tc)
                    userTestCasesFromFileCopy.pop(index)
                break
            break
        elif what == "Inputs":
            for tc in userTestCasesFromFileCopy:
                for input in tc.inputs:
                    if text in input:
                        index = userTestCasesFromFileCopy.index(tc)
                        userTestCasesFromFileCopy.pop(index)
                break
            break
        elif what == "ExpectedResults":
            for tc in userTestCasesFromFileCopy:
                for expected in tc.expecteds:
                    if text in expected:
                        index = userTestCasesFromFileCopy.index(tc)
                        userTestCasesFromFileCopy.pop(index)
                break
            break

#pre-removing test cases
for query in result:
    what = query[0].split()[0].replace('(', '').replace(')', '')
    action =  query.split()[1]
    text = query.split()[2].replace('"', '')
    if(action == "!contains" or action == "!="):
        removeTestCasesFromList(what, text)


for query in result:
    what = query.split()[0]
    action =  query.split()[1]
    text = query.split()[2].replace('"', '')



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