from abc import ABC, abstractmethod
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class ReportTable(Base):
    __tablename__ = 'Report'
    report_id = Column(Integer, primary_key=True, autoincrement=True)
    report_type_id = Column(Integer, ForeignKey('ReportType.report_type_id'), nullable=False)
    generated_date = Column(DateTime, nullable=False)
    details = Column(String)
    report_type = relationship('ReportTypeTable', back_populates='reports')


class Report(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def generateReport(self):
        pass
