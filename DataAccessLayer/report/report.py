from abc import ABC, abstractmethod

class Report(ABC):
    def __init__(self):
        self.content = ""

    def get_content(self):
        return self.content

    @abstractmethod
    def generate_report(self):
        pass

    @abstractmethod
    def print_report(self):
        pass
