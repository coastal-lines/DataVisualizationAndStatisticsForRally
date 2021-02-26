from pyral import Rally, rallyWorkset
from Project.RallyFolder import RallyFolder

class RallyInstance():
    def __init__(self, UserCredential):
        rally = Rally(server=UserCredential.server, user=UserCredential.user, password=UserCredential.password)
        self.rally = rally