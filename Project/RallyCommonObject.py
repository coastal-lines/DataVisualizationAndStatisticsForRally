from Project.UserCredential import UserCredential
from Project.RallyInstance import RallyInstance
from Project.RallyFolder import RallyFolder
from pyral import Rally, rallyWorkset

class RallyCommonObject():
    rally = None
    rootFolder = None

    def __init__(self, server, login, password, workspace, project, folder):
        self.user = UserCredential(server, login, password)
        self.rally = RallyInstance(user).rally
        self.rally.setWorkspace(workspace)
        self.rally.setProject(folder)
        self.rootFolder = RallyFolder(rally ,'FormattedID = "' + folder + '"').testFolder

"""
    def getRally():
        return self.rally

    def getRootFolder(self):
        return self.rootFolder
"""