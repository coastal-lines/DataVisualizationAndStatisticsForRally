class TestCase():
    #def __init__(self, formattedID, name, preConditions, inputs, expecteds):
    def __init__(self, formattedID, name, preConditions, inputs, expecteds, mainFolderName, rootFolderName, productArea, productSubarea, method, testFolder):
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