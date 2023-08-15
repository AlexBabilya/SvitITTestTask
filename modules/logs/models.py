from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from modules.database import Base


class LogEntry(Base):
    __tablename__ = 'log_entries'

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    message = Column(String, nullable=False)
