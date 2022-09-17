from typing import List, Union, Optional
from pydantic import BaseModel


class AchievementBase(BaseModel):
    pass

class AchievementCreate(AchievementBase):
    pass

class Achievement(AchievementBase):
    id: int
    name: str
    image: str

    class Config:
        orm_mode = True

class ScheduleBase(BaseModel):
    pass

class ScheduleCreate(ScheduleBase):
    pass

class Schedule(ScheduleBase):
    id = int
    schedulestart = str
    schedulestop = str

    class Config:
        orm_mode = True

class RoomBase(BaseModel):
    name = str

class RoomCreate(RoomBase):
    pass

class Room(RoomBase):
    id = int
    status = str
    energyhistory = []
    energyfuture = []
    schedules = []

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    email: str
    password: str
    is_active: bool
    address: Optional[str]
    overallenergyhistory: Optional[int]
    moneysaved: Optional[int]
    co2saved: Optional[int]
    achievements = []
    rooms = []
class User(UserBase):
    id: int
    is_active: bool
    address: Optional[str]
    overallenergyhistory: Optional[int]
    moneysaved: Optional[int]
    co2saved: Optional[int]
    achievements = []
    rooms = []

    class Config:
        orm_mode = True