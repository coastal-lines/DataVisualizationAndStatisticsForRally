import pickle

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

l = None
with open(r'C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\listTestCases.data', 'rb') as file:
    l = pickle.load(file)
    t=0

print(len(l))

query = input("Enter query: \n")

y=6