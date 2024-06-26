from sqlalchemy import Column, String, DateTime, Integer, Float
from src.database.base import Base
from datetime import datetime, timezone
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

class SportSessionModel(Base):
    __tablename__ = 'sport_session'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user = Column(UUID(as_uuid=True), nullable=False)
    trainingDayId = Column(UUID(as_uuid=True), nullable=False)
    FTP = Column(Float(), nullable=False)
    VO = Column(Float(), nullable=False)
    RPM = Column(Float(), nullable=False)
    KCAL = Column(Float(), nullable=False)
    startDate = Column(DateTime(), default=datetime.now(timezone.utc) )
    endDate = Column(DateTime(), default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc) )