from pyral import Rally, rallyWorkset

class RallyFolder():
    def __init__(self, rally, query):
        testFolderRequest = rally.get('TestFolder', fetch=True, projectScopeDown=True, query=query)
        testFolder = testFolderRequest.next()
        self.testFolder = testFolder