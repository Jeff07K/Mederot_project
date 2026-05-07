from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone

Base = declarative_base()


class Medarot(Base):
    __tablename__ = "medarots"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50), nullable=False)          # Shooter, Fighter, etc.
    medal_type = Column(String(50), nullable=False)    # Beetle, Stag, etc.
    attack_power = Column(Float, nullable=False)
    is_deleted = Column(Boolean, default=False)        # Soft delete
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))


class Medafighter(Base):
    __tablename__ = "medafighters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    rank = Column(String(50), nullable=False)          # Beginner, Intermediate, etc.
    specialty = Column(String(100), nullable=False)
    wins = Column(Integer, default=0)
    is_deleted = Column(Boolean, default=False)        # Soft delete
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))