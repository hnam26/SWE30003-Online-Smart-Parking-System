from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .reportType import ReportType

Base = declarative_base()


class Report(Base):
    __tablename__ = 'Report'
    report_id = Column(Integer, primary_key=True, autoincrement=True)
    report_type_id = Column(Integer, ForeignKey('ReportType.report_type_id'), nullable=False)
    generated_date = Column(DateTime, nullable=False)
    details = Column(String)
    report_type = relationship('ReportType', back_populates='reports')
