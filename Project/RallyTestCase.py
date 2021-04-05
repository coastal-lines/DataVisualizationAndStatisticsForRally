class TestCase():
    #def __init__(self, formattedID, name, preConditions, inputs, expecteds):
    def __init__(self, formattedID, name, preConditions, inputs, expecteds, mainFolderName, rootFolderName, project, productArea, productSubarea, method, testFolder, isAutomated):
        self.formattedID = formattedID
        self.name = name
        self.preConditions = preConditions
        self.inputs = inputs
        self.expecteds = expecteds
        self.mainFolderName = mainFolderName
        self.rootFolderName = rootFolderName
        self.project = project
        self.productArea = productArea
        self.productSubarea = productSubarea
        self.method = method
        self.testFolder = testFolder
        self.isAutomated = isAutomated
