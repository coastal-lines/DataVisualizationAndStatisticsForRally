from Project.RallyTestCaseSteps import RallyTestCaseSteps

class RallyTestCase():
    test_case = None
    steps = None
    listInputs = []
    listExpectedResult = []

    def getTestCaseByFormattedID(formattedID):
        for test_case in test_cases:
            print(test_case.FormattedID)
            print(test_case.Name)
            if(test_case.FormattedID == formattedID):
                return test_case
    
    def getStepsFromTestCase():
        steps = RallyTestCaseSteps(test_case)

    def getListInputs():
        listInputs = RallyTestCaseSteps(test_case)