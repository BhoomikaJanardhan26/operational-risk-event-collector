from sqlalchemy import Column, Integer, String, Text
from services.db import Base

class RiskLog(Base):
    __tablename__ = "risk_logs"

    id = Column(Integer, primary_key=True, index=True)
    input_text = Column(Text)
    response = Column(Text)
    created_at = Column(String)