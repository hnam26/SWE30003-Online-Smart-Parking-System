from abc import ABC, abstractmethod

class Report(ABC):
    def __init__(self, title):
        self.title = title
        self.content = ""

    def getTitle(self):
        return self.title

    def getContent(self):
        return self.content

    @abstractmethod
    def generateReport(self):
        pass

    def formatReport(self):
        return f"Title: {self.title}\nContent: {self.content}"
