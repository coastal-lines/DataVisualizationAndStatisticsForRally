from pyral import Rally, rallyWorkset

class RallyWorkspace():
    rootWorkspace = None

    def __init__(self, workspaces, workspaceName, projectName, rally):
        self.workspaces = workspaces
        self.projectName = projectName
        self.workspaceName = self.getWorkspace(workspaceName)
        self.projectName = self.getProjectName(rally)

    #а нахер вообще искать, если можно сразу задать имя???
    #можно переделать класс в поиск проекта или воркспейса по имени
    def getWorkspace(self, workspaceName):
        for ws in self.workspaces:
            if(ws.Name == workspaceName):
                self.rootWorkspace = ws
                break
        return self.rootWorkspace.Name

    def getProjectName(self, rally):
        projects = rally.getProjects(workspace = self.rootWorkspace.Name)
        rootProject = None
        for pr in projects:
            print(pr.Name)
            if(pr.Name == self.projectName):
                print(pr);
                rootProject = pr
                break
        return rootProject.Name
