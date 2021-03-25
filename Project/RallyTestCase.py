class TestCase():
    def __init__(self, formattedID, name, preConditions, inputs, expecteds):
        self.formattedID = formattedID
        self.name = name
        self.preConditions = preConditions
        self.inputs = inputs
        self.expecteds = expecteds