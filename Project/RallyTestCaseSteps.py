class RallyTestCaseSteps():
    listInputs = []
    listExpectedResult = []

    def __ini__(self, test_case):
        self.listInputs = initInputs(test_case)
        self.listExpectedResult = initResults(test_case)

    def initInputs(test_case):
        list_steps = None
        print(test_case.FormattedID)
        print(test_case.Name)
        list_steps = test_case.Steps
        for step in list_steps:
            listInputs.append(step.Input)
            print(step.Input)

    def initResults(test_case):
        list_steps = None
        print(test_case.FormattedID)
        print(test_case.Name)
        list_steps = test_case.Steps
        for expectedResults in list_steps:
            listExpectedResult.append(expectedResults.ExpectedResult)
            print(expectedResults.ExpectedResult)
