from pyral import Rally, rallyWorkset
import pickle

class TestCase():
    def __init__(self, formattedID, name, preConditions, inputs, expecteds):
        self.formattedID = formattedID
        self.name = name
        self.preConditions = preConditions
        self.inputs = inputs
        self.expecteds = expecteds

listTC = []



rally = Rally(server=server, user=user, password=password)
rally.setWorkspace(workspace)
rally.setProject(project)

query = 'FormattedID = %s'
test_folder_req = rally.get('TestFolder', fetch=True, projectScopeDown=True, query=query % 'TF23805')
test_folder = test_folder_req.next()
test_cases = test_folder.TestCases

for tc in test_cases:
    formattedID = tc.FormattedID
    name = tc.Name
    description = tc.Description

    inputs  = []
    expecteds = []

    list_steps = tc.Steps
    for i in list_steps:
        inputs.append(i.Input)
        expecteds.append(i.ExpectedResult)

    listTC.append(TestCase(formattedID, name, description, inputs, expecteds))


with open(r'C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\listTestCases.data', 'w+b') as file:
    pickle.dump(listTC, file)

#with open(r'C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\listTestCases.data', 'rb') as file:
 #   l = pickle.load(file)

a = 0