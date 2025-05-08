from sqlalchemy import Column, String, Integer, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Base2= declarative_base()

class ProductionInfo(Base):
    __tablename__ = 'production_info'

    date = Column(DateTime, primary_key=True, nullable=False)
    part_name = Column(String, nullable=False)
    die_qty = Column(Integer, nullable=False)
    ot = Column(Integer, nullable=True)
    tea = Column(Integer, nullable=True)
    water = Column(Integer, nullable=True)
    water_payment = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=func.now())


class dieInfo(Base2):
    __tablename__ = 'die_info'

    part_name = Column(String, primary_key=True, nullable=False)
    hr_qty = Column(Integer, nullable=False)
    qty_price = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=func.now())
