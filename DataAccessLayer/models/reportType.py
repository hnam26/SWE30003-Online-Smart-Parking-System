from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .report import Report

Base = declarative_base()


class ReportType(Base):
    __tablename__ = 'ReportType'
    report_type_id = Column(Integer, primary_key=True, autoincrement=True)
    type_name = Column(String(50), nullable=False)
    reports = relationship('Report', back_populates='report_type')
