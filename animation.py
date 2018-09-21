class surface():
    def __init__(self, scaryFunction: function):
        self.definition = scaryFunction
    def evaluate(self, *args):
        return self.definition(args)
