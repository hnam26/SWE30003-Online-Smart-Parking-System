from abc import ABC, abstractmethod

class Report(ABC):
    def __init__(self):
        self.content = ""

    def getContent(self):
        return self.content

    @abstractmethod
    def generateReport(self):
        pass

    @abstractmethod
    def printReport(self):
        pass
