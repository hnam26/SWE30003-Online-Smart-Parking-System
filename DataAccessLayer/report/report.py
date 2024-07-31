from abc import ABC, abstractmethod


class Report(ABC):
    def __init__(self):

    @abstractmethod
    def generateReport(self):
        pass
