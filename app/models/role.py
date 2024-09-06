import pytz
from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Definir la zona horaria
TIME_ZONE = pytz.utc


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(TIME_ZONE),
        nullable=False,
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(TIME_ZONE),
        onupdate=func.now(TIME_ZONE),
        nullable=False,
    )
