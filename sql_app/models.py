from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table, Enum
from sqlalchemy.orm import relationship

from .database import Base

userstoachievements = Table(
    "userstoachievements",
    Base.metadata,
    Column("user", ForeignKey("users.id")),
    Column("achievement", ForeignKey("achievements.id")),
)

userstorooms = Table(
    "userstorooms",
    Base.metadata,
    Column("user", ForeignKey("users.id")),
    Column("room", ForeignKey("rooms.id")),
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    address = Column(String)
    overallenergyhistory = Column(Integer, default=0)
    moneysaved = Column(Integer, default=0)
    co2saved = Column(Integer, default=0)
    achievements = relationship("Achievement", secondary=userstoachievements)
    rooms = relationship("Room", secondary=userstorooms)

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String, index=True, default="ON")
    energyhistory = relationship("histories", backref="parents")
    energyfuture = relationship("histories", backref="parents")
    schedules = relationship("schedules", backref="rooms")

    def __init__(self, energyhistory, energyfuture):
        self.energyhistory = energyhistory
        self.energyfuture = energyfuture

class Achievement(Base):
    __tablename__ = "achievements"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, default="New Achievement")
    image = Column(String)

class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    schedulestart = Column(String, index=True)
    schedulestop = Column(String, index=True)

class Historiy(Base):
    __tablename__ = "histories"

    id = Column(Integer, primary_key=True, index=True)
    month = Column(String, index=True)
    value = Column(String, index=True)