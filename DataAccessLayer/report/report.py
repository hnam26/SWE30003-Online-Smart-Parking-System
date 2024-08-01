from abc import ABC, abstractmethod


class Report(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def generateReport(self):
        pass
