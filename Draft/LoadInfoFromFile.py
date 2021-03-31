import pickle

class TestCase():
    def __init__(self, formattedID, name, preConditions, inputs, expecteds):
        self.formattedID = formattedID
        self.name = name
        self.preConditions = preConditions
        self.inputs = inputs
        self.expecteds = expecteds

l = None
with open(r'C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\listTestCases.data', 'rb') as file:
    l = pickle.load(file)
    t=0

print(len(l))

query = input("Enter query: \n")

y=6