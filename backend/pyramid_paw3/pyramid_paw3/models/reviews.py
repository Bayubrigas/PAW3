from sqlalchemy import Column, Integer, Text, String, DateTime, func
from .meta import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    user_input = Column(Text, nullable=False)
    sentiment = Column(String(20), nullable=False)
    key_points = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
