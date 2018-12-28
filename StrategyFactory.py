class StrategyFactory():
    def __init__(self):
        pass

    def getStrategyClass(self,fileName):
        module = __import__(fileName)
        class_ = getattr(module, fileName)
        return class_()
